from dotenv import load_dotenv
from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables import RunnableSequence

load_dotenv()

model = ChatOpenAI(model='gpt-4o-mini')

prompt = ChatPromptTemplate.from_template("""
    You are technical recruiter.
    Analyze the following job description.

    job description: {job_description}

    identify:
    1.Required technical skills
    2.Required years of experience
    3.required cloud technologies
    4.required ML/AI Skills
    5.important responsibilites

    givr the result in a clear format
""")

parser = StrOutputParser()

chain = RunnableSequence(prompt,model,parser)

job_description = input("Enter you job description: ")

result = chain.invoke({
    "job_description": job_description
})

print(result)