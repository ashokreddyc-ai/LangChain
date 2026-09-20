from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain_openai.chat_models import ChatOpenAI

load_dotenv()

llm = ChatOpenAI(model="gpt-4o-mini")

Prompt_template = PromptTemplate.from_template(
    """
    Generate {count} interview questions on {technology} for a {level} candidate.
    for every question:
    1.Give the question
    2.Give a simple answer
    """
)

count = input("Enter Number of questions: ")
technology = input("Enter the technology: ") 
level =  input("Enter the level: ")

prompt = Prompt_template.invoke({"count":count,"technology":technology,"level":level})

respones = llm.invoke(prompt)

print(respones.content)