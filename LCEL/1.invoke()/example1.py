from langchain_core.prompts import PromptTemplate
from langchain_openai import ChatOpenAI
from langchain_core.output_parsers import StrOutputParser
from dotenv import load_dotenv

load_dotenv()

model = ChatOpenAI(model="gpt-4o-mini")

prompt = PromptTemplate.from_template("Exaplain {topic} is very simple english")

parser = StrOutputParser()

chain = prompt | model | parser

topic = input("Enter required topic: ")

result = chain.invoke({"topic":topic})

print(result)