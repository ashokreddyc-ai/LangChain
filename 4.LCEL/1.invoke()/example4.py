from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain_openai import ChatOpenAI
from langchain_core.output_parsers import StrOutputParser

load_dotenv()

model = ChatOpenAI(model="gpt-4o-mini")

prompt = PromptTemplate.from_template("""
        Generate {count} {level} interview questions about {technology}. use simple english and provide answers as well
""")

parser = StrOutputParser()

chain = prompt | model | parser

technology = input("Enter technology: ")
level = input("Enter your level: ")
count = input("Enter how many questions are required: ")

result = chain.invoke({"technology":technology,"level":level,"count":count})

print(result)