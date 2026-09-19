from dotenv import load_dotenv

from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser

load_dotenv()

model = ChatOpenAI(model="gpt-5.6-luna")

prompt = ChatPromptTemplate.from_template(
    "Explain {topic} in simple English."
)

parser = StrOutputParser()

chain = prompt | model | parser

inputs = [
    {"topic": "Python"},
    {"topic": "SQL"},
    {"topic": "LangChain"},
    {"topic": "Docker"}
]

for index, response in chain.batch_as_completed(inputs):

    print("Index:", index)
    print("Response:", response)
    print("-" * 50)