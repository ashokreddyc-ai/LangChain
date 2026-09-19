from dotenv import load_dotenv
from langchain_core.output_parsers import StrOutputParser
from langchain_openai import ChatOpenAI
from langchain_core.prompts import PromptTemplate

load_dotenv()

model = ChatOpenAI(model="gpt-5.6-luna")

prompt = PromptTemplate.from_template(""" Give 5 beginner interview questions about {technology}""")

parser = StrOutputParser()

chain = prompt | model | parser

inputs = [{"technology":"Python"},{"technology":"Java"},{"technology":"SQL"}]

results = chain.batch(inputs=inputs,config={"max_concurrency":1})

for technology,result in zip(['Python','Java','SQL'],results):
    print("\n====================")
    print(technology)
    print("======================")
    print(result)