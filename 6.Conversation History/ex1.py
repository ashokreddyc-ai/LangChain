from dotenv import load_dotenv
from langchain_core.messages import HumanMessage,AIMessage,SystemMessage
from langchain_openai import ChatOpenAI

load_dotenv()

llm = ChatOpenAI(model="gpt-4o-mini",temperature=0)

response1 = llm.invoke("my names is ashok")

response2 = llm.invoke("""what is my name?
                        if my name is not availabe in the supplied conversation, say i do not know""")

print("\nsecondresponse")

print(response2.content)