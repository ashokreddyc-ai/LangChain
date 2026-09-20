from dotenv import load_dotenv
from langchain_core.messages import HumanMessage,AIMessage,SystemMessage
from langchain_openai.chat_models import ChatOpenAI

load_dotenv()

llm = ChatOpenAI(model="gpt-4o-mini")

messages = [
    SystemMessage("Your are help full python teacher"),
    HumanMessage("Explain loops"),
    AIMessage("Loops are very important in python"),
    HumanMessage("Explain condational loops")
]

response = llm.invoke(messages)
print(response.content)