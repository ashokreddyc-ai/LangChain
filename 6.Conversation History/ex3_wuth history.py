from dotenv import load_dotenv
from langchain_core.messages import HumanMessage,AIMessage,SystemMessage
from langchain_openai import ChatOpenAI

load_dotenv()

llm = ChatOpenAI(model='gpt-4o-mini')

question = HumanMessage(content=
    """
    what is my name?
    if my name is not available in the supplied conversation,say i do not know
    """
)

messages = [HumanMessage(content='my name is ashok'),
            AIMessage(content="nice to meet you"),
            question]

response = llm.invoke(messages)
print(response.content)