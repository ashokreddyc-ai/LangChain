from dotenv import load_dotenv
from langchain_openai.chat_models import ChatOpenAI
from langchain_core.prompts import PromptTemplate

load_dotenv()

llm = ChatOpenAI(model="gpt-4o-mini")

template = PromptTemplate.from_template("Give me simple recipe for {dish}. Explain it step by step")

dish = input("Enter dish")

prompt = template.invoke({"dish":dish})

result = llm.invoke(prompt)

print(result.content)

