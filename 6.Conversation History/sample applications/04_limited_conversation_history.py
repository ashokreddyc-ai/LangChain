from langchain_openai import ChatOpenAI
from langchain_core.messages import HumanMessage, AIMessage
from dotenv import load_dotenv

load_dotenv()

llm = ChatOpenAI(model="gpt-4o-mini",temperature=0)

conversation_history = []

while True:

    user_input = input("You: ")

    if user_input.lower() == "exit":
        break

    conversation_history.append(HumanMessage(content=user_input))

    # Keep only the latest 6 messages
    recent_history = conversation_history[-6:]

    response = llm.invoke(recent_history)

    conversation_history.append(AIMessage(content=response.content))

    print("Assistant:", response.content)

    print("\nCurrent history:")
    for message in conversation_history:
        print(message)