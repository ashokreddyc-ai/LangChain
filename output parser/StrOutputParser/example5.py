from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain_openai.chat_models import ChatOpenAI
from langchain_core.output_parsers import StrOutputParser

load_dotenv()

llm = ChatOpenAI(model='gpt-4.1-mini')

template = PromptTemplate.from_template("""
    Explain {topic} to {level} learner.
    requirements:
    1.use very simple english
    2.give 5 important points
    3.give one simple example
    """)

topic = input("Enter required topic: ")
level =  input("Enter you level: ")

prompt = template.invoke({"topic":topic,"level":level})

response = llm.invoke(prompt)

parser = StrOutputParser()

result = parser.invoke(response)

print(result)