from dotenv import load_dotenv
from langchain_openai import ChatOpenAI
from langchain_core.messages import HumanMessage,AIMessage,SystemMessage

load_dotenv()

llm = ChatOpenAI(model="gpt-4o-mini")

messages = [
    HumanMessage(content="My name is ashok"),
    AIMessage(content="Nice to meet you, ashok"),
    HumanMessage(content="What is my name")
]

response = llm.invoke(messages)
print(response.content)
