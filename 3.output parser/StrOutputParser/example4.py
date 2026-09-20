from dotenv import load_dotenv
from langchain_core.output_parsers import StrOutputParser
from langchain_openai.chat_models import ChatOpenAI
from langchain_core.prompts import PromptTemplate


load_dotenv()

llm = ChatOpenAI(model="gpt-4.1-mini")

template = PromptTemplate.from_template("""
    Give a simple recipe for {dish}
    Requirements:
    1.List ingredients
    2.Give step by steo procedure
    3.use simple english
    """)

dish = input("Enter your required dish: ")

prompt = template.invoke({"dish":dish})

response = llm.invoke(prompt)

parser = StrOutputParser()

result = parser.invoke(response)
print(result)