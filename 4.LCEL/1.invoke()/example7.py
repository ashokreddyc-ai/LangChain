from dotenv import load_dotenv
from langchain_core.output_parsers import StrOutputParser
from langchain_openai import ChatOpenAI
from langchain_core.prompts import PromptTemplate

load_dotenv()

model = ChatOpenAI(model="gpt-4o-mini")

prompt = PromptTemplate.from_template(
    """
    Explain {topic} to a {level} learner.

    Requirements:
    - Use very simple English
    - Give a simple definition
    - Give 5 important points
    - Give one real-world example
    - Give one-line conclusion
    """
)

parser = StrOutputParser()

topic = input("Enter topic: ")
level = input("Enter your level: ")

chain = prompt | model | parser

result = chain.invoke({"topic":topic,"level":level})

print(result)