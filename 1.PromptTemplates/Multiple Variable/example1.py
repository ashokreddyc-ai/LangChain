from dotenv import load_dotenv
from langchain_openai.chat_models import ChatOpenAI
from langchain_core.prompts import PromptTemplate

load_dotenv()

llm = ChatOpenAI(model="gpt-4o-mini")

Prompt_template = PromptTemplate.from_template('Explain {topic} in {Language} in {style}  style')

topic = input("Enter topic: ")
language = input("Enter Required Language: ")
style = input("Enter required style: ")

promt = Prompt_template.invoke({"topic":topic,"Language":language,"style":style})

result = llm.invoke(promt)

print(result.content)