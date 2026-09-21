from dotenv import load_dotenv
from langchain_core.output_parsers import StrOutputParser
from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.runnables import RunnableSequence

load_dotenv()

model = ChatOpenAI(model='gpt-4o-mini')

prompt = ChatPromptTemplate.from_template(
    """
    You are a payment gateway support assistant.

    Customer question:
    {question}

    Explain the answer in simple English.
    If there is a technical issue, also mention the likely reason.
    """
)

parser = StrOutputParser()

chain = RunnableSequence(prompt,model,parser)

question = input("Enter your question: ")

response = chain.invoke({'question':question})

print(response)
