from langchain_core.prompts import PromptTemplate
from langchain_openai.chat_models import ChatOpenAI
from dotenv import load_dotenv

load_dotenv()

llm = ChatOpenAI(model= "gpt-4o-mini")

prompt = PromptTemplate(template="Explain {topic} in simple terms")

topic = input("Enter the topic: ")

result = prompt.invoke({"topic":topic})

ai_message = llm.invoke(result)

print(ai_message.content)