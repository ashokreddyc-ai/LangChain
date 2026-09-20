from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain_openai.chat_models import ChatOpenAI

load_dotenv()

llm = ChatOpenAI(model="gpt-4o-mini")

topic = input("Enter topic: ")
level = input("Enter you level: ")


prompt_template = PromptTemplate.from_template(
    template="Explain {topic} at {level}",
    partial_variables={"topic":"python","level":"beginner"}
)

promt = prompt_template.invoke({"topic":topic,"level":level})

print(promt.to_string())