from dotenv import load_dotenv
from langchain_core.output_parsers import StrOutputParser
from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate

load_dotenv()

model = ChatOpenAI(model='gpt-5.6-luna')

for chunk in model.stream("Explain rag in simple English"):
    print(chunk.content, end="")