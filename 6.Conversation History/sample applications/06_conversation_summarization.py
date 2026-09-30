from langchain_openai import ChatOpenAI
from langchain_core.messages import HumanMessage,AIMessage,SystemMessage
from dotenv import load_dotenv

load_dotenv()

llm = ChatOpenAI(model='gpt-4o-mini',temperature=0)

#system instructions for the chatbot
system_message = SystemMessage(content=""" 
Your are helpful python tutor.
Explain python concepts in simple english.
keep your answer concise.
""")

#store recent conversation
conversation_history = []
#store summary of old conversation
conversation_summary = ""
#keep only the latest 4 messages
window_size = -4

while True:
    user_input = input("\nyou: ")
    if user_input.lower() == exit:
        break
    #add user messages
    conversation_history.append(HumanMessage(content=user_input))
    #take recent messages only
    recent_history =conversation_history[window_size:]
    #build message for chat
    messages = [system_message]

    #add older conversation summary if available
    if conversation_summary:
        messages.append(SystemMessage(content=f"""important context from the earlier conversation: {conversation_summary}"""))

    #add recent conversation
    messages.extend(recent_history)
    #call llm
    response = llm.invoke(messages)
    print("\nAI: ",response.content)

    #store ai response
    conversation_history.append(AIMessage(content=response.content))

    # if hostory becomes larger than window size, summarize the older messages
    if len(conversation_history)>window_size:
        #messages outside of the current window
        old_messages = conversation_history[:window_size]

        summary_prompt = [SystemMessage(
            content="""
            summarize the important information from this conversation.
            keep:
            - important user information
            - important prederences
            - important topic discusses
            - important decisions or requirements
            remove:
            - greetings
            - repeated information
            - unimportant details
            return a short summary in plain english    
            """
        )]
    #include previous summary if one exits
    if conversation_summary:
        summary_prompt.append(SystemMessage(content=f"""existing summary: {conversation_summary}"""))

    #add old messages
    summary_prompt.extend(old_messages)
    #generate updated summary
    summary_response = llm.invoke(summary_prompt)
    conversation_summary = summary_response.content
            # Keep only recent messages in active history
    conversation_history = conversation_history[window_size:]

    print("\n--- Summary Updated ---")
    print(conversation_summary)

print("\nMessages currently stored:",len(conversation_history))