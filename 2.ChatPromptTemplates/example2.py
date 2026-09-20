from dotenv import load_dotenv
from langchain_openai import ChatOpenAI
from langchain_core.messages import HumanMessage,AIMessage,SystemMessage
from langchain_core.prompts import ChatPromptTemplate

load_dotenv()

llm = ChatOpenAI(model="gpt-4o-mini")

template = ChatPromptTemplate.from_messages(messages=
    [
    ("system","Your are help full python teacher"),
    ("human","Explain loops"),
    ("ai","Loops are very important in python"),
    ("human","Explain condational loops")
    ])


prompt = template.invoke({})


for message in prompt.messages: #to check how many messages are in the template
    print(type(message).__name__, ":", message.content)

response = llm.invoke(prompt)
print(response.content)