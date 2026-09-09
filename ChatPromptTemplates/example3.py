from dotenv import load_dotenv
from langchain_openai import ChatOpenAI
from langchain_core.messages import HumanMessage,AIMessage,SystemMessage
from langchain_core.prompts import ChatPromptTemplate

load_dotenv()

llm = ChatOpenAI(model="gpt-4o-mini")

template = ChatPromptTemplate.from_messages(messages=
    [
    SystemMessage("Your are help full python teacher"),
    HumanMessage("Explain loops"),
    AIMessage("Loops are very important in python"),
    HumanMessage("Explain condational loops")
    ])


prompt = template.invoke({})


for message in prompt.messages: #to check how many messages are in the template
    print(type(message).__name__, ":", message.content)

response = llm.invoke(prompt)
print(response.content)