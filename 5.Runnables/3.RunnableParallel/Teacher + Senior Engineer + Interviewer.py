"""
We give the same question to three different "roles":

1.Teacher
2.Senior Engineer
3.Interviewer

For example:

"What is an API?"

Each LLM chain answers from a different perspective.
"""
from dotenv import load_dotenv
from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.runnables import RunnableParallel
from langchain_core.output_parsers import StrOutputParser

load_dotenv()


model = ChatOpenAI(model="gpt-4o-mini",temperature=0)


teacher_prompt = ChatPromptTemplate.from_template(
    """
    You are a teacher.

    Explain the following question to a beginner
    using simple English and a simple analogy.

    Question:
    {question}
    """
)


engineer_prompt = ChatPromptTemplate.from_template(
    """
    You are a senior software engineer.

    Explain the following question from a
    practical software engineering perspective.

    Question:
    {question}
    """
)


interviewer_prompt = ChatPromptTemplate.from_template(
    """
    You are a technical interviewer.

    Answer the following question as if a candidate
    with 4 years of experience is answering in an interview.

    Keep the answer concise but technically strong.

    Question:
    {question}
    """
)


parser = StrOutputParser()

teacher_chain = teacher_prompt | model | parser

engineer_chain = engineer_prompt | model | parser

interviewer_chain = interviewer_prompt | model | parser

parallel_chain = RunnableParallel(
    teacher=teacher_chain,
    engineer=engineer_chain,
    interviewer=interviewer_chain
)

question = input("Enter you technical question: ")

result = parallel_chain.invoke({"question": question})


print("\n========== TEACHER ==========")
print(result["teacher"])

print("\n========== ENGINEER ==========")
print(result["engineer"])

print("\n========== INTERVIEWER ==========")
print(result["interviewer"])