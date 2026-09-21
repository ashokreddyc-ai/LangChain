from dotenv import load_dotenv
from langchain_openai import ChatOpenAI
from langchain_core.runnables import RunnableLambda
from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import ChatPromptTemplate

load_dotenv()

model = ChatOpenAI(model='gpt-4o-mini')

prompt = ChatPromptTemplate.from_template("""
        Analyze this transaction:
        transaction: {transaction}

        Identify whether the transactions looks normal, suspicious, fraudulent.
        """)

def apply_check(response):
    if "fraud" in response.lower():
        return "HIGH RISK: Transaction requires manual review"
    elif "suspicious" in response.lower():
        return "MEDIUM RISK: Additional verification required"
    else:
        return "lower risk: Transaction looks normal"

risk_checker = RunnableLambda(apply_check)

parser = StrOutputParser()

chain = prompt | model | parser | risk_checker

result = chain.invoke({"transaction":"transaction of 95000 ruppes at 2:30 AM from a new device"})

print(result)