from dotenv import load_dotenv
from langchain_openai import ChatOpenAI
from langchain_core.messages import HumanMessage,AIMessage,SystemMessage
from langchain_core.prompts import ChatPromptTemplate

load_dotenv()

llm = ChatOpenAI(model="gpt-4o-mini")

template = ChatPromptTemplate.from_messages(messages=
    [
    ("system","Your are help full {subject} teacher. Explain python in simple english"),
    ("human","Explain {topic} with an example"),
    ])

subject = input("Enter required subject: ")
topic = input("Enter topic: ")


prompt = template.invoke({"subject":subject,"topic":topic})


response = llm.invoke(prompt)
print(response.content)