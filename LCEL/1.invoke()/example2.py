from langchain_openai import ChatOpenAI
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from dotenv import load_dotenv

load_dotenv()

llm = ChatOpenAI(model='gpt-4o-mini')

prompt = PromptTemplate.from_template(

    """
    Explain {topic} in very simple English.
    give:
    1.Simple definition
    2.Important points
    3.one Example
    """
)

parser = StrOutputParser()

chain = prompt | llm | parser

topic = input("Enter required topic: ")
result = chain.invoke({"topic": topic})
print(result)