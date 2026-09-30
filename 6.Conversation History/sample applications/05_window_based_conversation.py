from dotenv import load_dotenv
from langchain_core.messages import HumanMessage,AIMessage,SystemMessage
from langchain_openai import ChatOpenAI

load_dotenv()

model = ChatOpenAI(model='gpt-4o-mini',temperature=0)

#system message
system_message = SystemMessage(content=
                               """
                            You are python tutor.
                            explain concepts in simple english.
                            give example when useful
                            """)

#store complete conversation.
conversation_history = []

#number of message keep active in the window.
window_size = 4

while True:
    user_input = input("\nyou: ")
    if user_input.lower() == "exit":
        break

    #store user message
    conversation_history.append(HumanMessage(content=user_input))

    #get only recent messages
    recent_history = conversation_history[-window_size:] 
    #system message + recent message
    messages = [system_message] + recent_history
    #send to LLM
    response = model.invoke(messages)
    #store ai response
    conversation_history.append(AIMessage(content=response.content))

    print("AI:",response.content)

    print("\nTotal messages stored: ",len(conversation_history))
    print("message sent to llm: ",len(messages))
