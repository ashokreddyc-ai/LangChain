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

    # Add user message
    conversation_history.append(HumanMessage(content=user_input))

    # Send history to LLM
    response = llm.invoke(conversation_history)

    # Add AI response
    conversation_history.append(AIMessage(content=response.content))

    print("Assistant:", response.content)