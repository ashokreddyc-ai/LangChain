from dotenv import load_dotenv
from langchain_core.output_parsers import StrOutputParser
from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate

load_dotenv()

model = ChatOpenAI(model='gpt-5.6-luna')

prompt = ChatPromptTemplate.from_template("Explain {topic} in simple english")

chain = prompt | model

topic = input("Enter required topic: ")

for chunk in chain.stream({"topic":topic}):
    print(chunk.content,end='')