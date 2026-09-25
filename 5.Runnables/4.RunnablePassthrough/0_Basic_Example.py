from langchain_core.runnables import RunnablePassthrough,RunnableParallel
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_openai import ChatOpenAI
from dotenv import load_dotenv

load_dotenv()

model = ChatOpenAI(model='gpt-4o-mini',temperature=0)

prompt = ChatPromptTemplate.from_template("""
        Answer this question in simple english: {question}
        """)

chain = RunnableParallel(
    question = RunnablePassthrough(),
    answer = prompt | model | StrOutputParser()
)

input_date = input("Enter your question: ")

result = chain.invoke({"question":input_date})

print(result['question'])
print("*"*100)
print(result['answer'])
