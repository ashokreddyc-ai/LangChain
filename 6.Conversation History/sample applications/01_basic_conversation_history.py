from dotenv import load_dotenv
from langchain_openai import ChatOpenAI

load_dotenv()

llm = ChatOpenAI(model='gpt-4o-mini')

conversation_history = []

while True:
    user_input = input('you: ')

    if user_input.lower() == "exit":
        break

    #store user message
    conversation_history.append(f"user: {user_input}")

    #send complete history to LLM
    prompt = "\n".join(conversation_history)
    response = llm.invoke(prompt)

    #store ai response
    conversation_history.append(f"assistanf: {response.content}")

    print("Assistant: ",response.content)

