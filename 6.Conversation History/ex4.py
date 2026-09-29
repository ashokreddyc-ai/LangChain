from langchain_core.messages import HumanMessage
from langchain_openai import ChatOpenAI
from dotenv import load_dotenv

load_dotenv()

model = ChatOpenAI(model='gpt-4o-mini',temperature=0)

#complete history
messages =[]

#max recent messages sent to model
max_messages = 4

while True:
    user_input = input("\nyou: ")

    if user_input.lower() == "exit":
        print("chat ended")
        break
    # add user message to complete history
    messages.append(HumanMessage(content=user_input))

    #select recent messages
    recent_messages = messages[-max_messages:]

    #send only recent history
    response = model.invoke(recent_messages)

    print("AI: ",response.content,)

    #store ai response in complete history
    messages.append(response)