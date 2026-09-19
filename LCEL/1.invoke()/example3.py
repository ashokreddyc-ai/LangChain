from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain_openai import ChatOpenAI
from langchain_core.output_parsers import StrOutputParser

load_dotenv()

model = ChatOpenAI(model='gpt-4o-mini')

prompt = PromptTemplate.from_template("""
    Explain {topic} in {language} for a {level} learner
    give one simple example
""")

parser = StrOutputParser()

chain = prompt | model | parser

topic = input("Enter required topic: ")
language = input("Enter required language: ")
level = input("Enter learner level: ")

result = chain.invoke({"topic":topic,"language":language,"level":level})

print(result)