from langchain_openai import ChatOpenAI
from dotenv import load_dotenv

load_dotenv()

llm = ChatOpenAI(
    model="gpt-4o-mini",
    temperature=0
)

conversation_history = []

while True:

    user_input = input("You: ")

    if user_input.lower() == "exit":
        break

    # Add user message
    conversation_history.append(
        {
            "role": "user",
            "content": user_input
        }
    )

    # Create conversation text
    conversation_text = ""

    for message in conversation_history:
        conversation_text += (message["role"] + ": " + message["content"] + "\n")

    response = llm.invoke(conversation_text)

    # Add assistant message
    conversation_history.append(
        {
            "role": "assistant",
            "content": response.content
        }
    )

    print("Assistant:", response.content)