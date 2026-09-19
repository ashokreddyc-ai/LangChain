from dotenv import load_dotenv
from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import ChatPromptTemplate
from langchain_openai import ChatOpenAI

load_dotenv()

model = ChatOpenAI(model='gpt-5.6-luna')

prompt = ChatPromptTemplate.from_template("Explain {topic} in simple english")

parser = StrOutputParser()

chain = prompt | model | parser

topic = input("Enter required topic: ")

for chunk in chain.stream({"topic":topic}):
    print(chunk, end='')