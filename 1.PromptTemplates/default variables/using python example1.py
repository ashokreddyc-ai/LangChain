from dotenv import load_dotenv
from langchain_openai.chat_models import ChatOpenAI
from langchain_core.prompts import  PromptTemplate

load_dotenv()

topic = input("Enter topic: ") or "python"
level = input("Enter your required level: ") or "beginner"


llm = ChatOpenAI(model="gpt-4o-mini")

promt_template = PromptTemplate.from_template("Explain {topic} at {level}")

prompt = promt_template.invoke({'topic':topic,"level":level})

print("========================")
print(prompt.to_string())
print()
print("======================")

response = llm.invoke(prompt)

print(response.content)