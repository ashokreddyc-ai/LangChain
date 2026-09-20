from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain_openai.chat_models import ChatOpenAI
from langchain_core.output_parsers import StrOutputParser

load_dotenv()

llm = ChatOpenAI(model='gpt-4.1-mini')

template = PromptTemplate.from_template("""Generate 5 {level} interview questions about {technology} use simple english""")

level = input("Enter your experience level: ")
technology = input("Enter your required technology: ")


prompt = template.invoke({"level":level,"technology":technology})

response = llm.invoke(prompt)

parser = StrOutputParser()

result = parser.invoke(response)

print(result)