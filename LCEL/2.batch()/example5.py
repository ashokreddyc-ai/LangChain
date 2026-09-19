from dotenv import load_dotenv
from langchain_core.prompts import ChatPromptTemplate
from langchain_openai import ChatOpenAI
from langchain_core.output_parsers import StrOutputParser

load_dotenv()

model = ChatOpenAI(model='gpt-4o-mini')

prompt = ChatPromptTemplate.from_template("Explain {topic} in simple english")

parser = StrOutputParser()

chain = prompt | model | parser

inputs = [
        {"topic":"python"},
        {"topic":'LCEL'},
        {"topic":""}
        ]

results = chain.batch(inputs=inputs,config={"max_concurrency":2},return_exceptions=True)

for input_data, result in zip(inputs, results):
    print(input_data["topic"])
    print(result)
    print("*"*100)