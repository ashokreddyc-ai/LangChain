from dotenv import load_dotenv
from langchain_openai.chat_models import ChatOpenAI
from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import ChatPromptTemplate

load_dotenv()

llm = ChatOpenAI(model="gpt-4.1-mini")

template = ChatPromptTemplate.from_messages(
    [
        ('system',"act as python expert"),
        ("human","enter python {topic} topic")
    ]
)

topic = input("Enter the python topic")

prompt = template.invoke({"topic":topic})

response = llm.invoke(prompt)

parser = StrOutputParser()

output = parser.invoke(response)

print(output)