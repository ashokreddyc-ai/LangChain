from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain_openai.chat_models import ChatOpenAI

load_dotenv()

llm = ChatOpenAI(model="gpt-4o-mini")

topic = input("Enter topic: ")
level = input("Enter your level: ")

prompt_template = PromptTemplate.from_template(
    template="Explain {topic} at {level} level",
    partial_variables={"topic": "python","level": "beginner"})

values = {}

if topic:
    values["topic"] = topic

if level:
    values["level"] = level

prompt = prompt_template.invoke(values)

print(prompt.to_string())