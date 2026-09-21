from langchain_core.prompts import PromptTemplate
from langchain_openai import ChatOpenAI
from langchain_core.output_parsers import StrOutputParser
from dotenv import load_dotenv
from langchain_core.runnables import RunnableSequence

load_dotenv()

model = ChatOpenAI(model='gpt-4o-mini')

prompt = PromptTemplate.from_template(template="Explain {topic} in simple english",
                                      input_variable=['topic'])

parser = StrOutputParser()

chain = RunnableSequence(prompt,model,parser)

response = chain.invoke({"topic":"python"})

print(response)