from dotenv import load_dotenv
from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import ChatPromptTemplate
from langchain_openai import ChatOpenAI

load_dotenv()

model = ChatOpenAI(model='gpt-5.6-luna')

prompt = ChatPromptTemplate.from_template(
    """
    You are a helpful AI assistant.
    Answer the following question in simple English:
    {question}
    """)

parser = StrOutputParser()

chain = prompt | model | parser

question = input("Ask as question: ")

for chunk in chain.stream({"question":question}):
    print(chunk,end='')