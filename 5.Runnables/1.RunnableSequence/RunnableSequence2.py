from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain_core.runnables import RunnableSequence
from langchain_openai import ChatOpenAI
from langchain_core.output_parsers import StrOutputParser

load_dotenv()

model = ChatOpenAI(model='gpt-4o-mini')

prompt = PromptTemplate.from_template("Explain {topic} in simple english",input_variable=['topic'])

parser = StrOutputParser()

chain = RunnableSequence(prompt,model,parser)

response = chain.invoke({"topic":"excel"})

print(response)