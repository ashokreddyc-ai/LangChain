from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.runnables import RunnableParallel
from dotenv import load_dotenv
from langchain_core.output_parsers import StrOutputParser

load_dotenv()

llm = ChatOpenAI(model="gpt-4o-mini",temperature=0)

concept_prompt = ChatPromptTemplate.from_template(
    """
    Explain this topic conceptually.

    Topic:
    {topic}
    """
)

practical_prompt = ChatPromptTemplate.from_template(
    """
    Explain how this topic is used in real-world
    software applications.

    Topic:
    {topic}
    """
)

interview_prompt = ChatPromptTemplate.from_template(
    """
    Explain this topic as an interview answer
    for a developer with 4 years of experience.

    Topic:
    {topic}
    """
)

parser = StrOutputParser()

concept_chain = concept_prompt | llm | parser

practical_chain = practical_prompt | llm | parser

interview_chain = interview_prompt | llm | parser

parallel_chain = RunnableParallel(
    concept=concept_chain,
    practical=practical_chain,
    interview=interview_chain
)


final_prompt = ChatPromptTemplate.from_template(
    """
    You are a senior technical trainer.

    Using the following three analyses, create
    one clear and accurate final explanation.

    CONCEPTUAL ANALYSIS:
    {concept}

    PRACTICAL ANALYSIS:
    {practical}

    INTERVIEW ANALYSIS:
    {interview}

    Make the final answer:
    - technically accurate
    - easy to understand
    - suitable for a 4-year experience developer
    """
)

final_chain = final_prompt | llm | parser

complete_chain = (
    parallel_chain
    | final_chain
)

result = complete_chain.invoke({
    "topic": "Microservices"
})

print("\n========== FINAL ANSWER ==========\n")

print(result)