from dotenv import load_dotenv
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_openai import ChatOpenAI

load_dotenv()

prompt = ChatPromptTemplate.from_template("""
Answer the question using the context below.

Context:
{context}

Question:
{question}
""")

model = ChatOpenAI(model="gpt-4o-mini")

parser = StrOutputParser()

rag_chain = prompt | model | parser

inputs = [
    {
        "context": "PayU supports multiple payment gateways.",
        "question": "What does PayU support?"
    },
    {
        "context": "A transaction can fail because of insufficient funds.",
        "question": "Why can a transaction fail?"
    },
    {
        "context": "Refunds are generally processed after the merchant initiates them.",
        "question": "How is a refund initiated?"
    }
]

answers = rag_chain.batch(
    inputs,
    config={
        "max_concurrency": 3
    }
)

for answer in answers:
    print(answer)