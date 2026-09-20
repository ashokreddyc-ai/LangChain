from dotenv import load_dotenv
from langchain_openai.chat_models import ChatOpenAI
from langchain_core.prompts import PromptTemplate

load_dotenv()

llm = ChatOpenAI(model="gpt-4o-mini")

prompt_template = PromptTemplate.from_template("""
        Create a simple travel plan for {place}.
        duration: {days} days
        budget:{budget}
        include:
        1.Place to visit
        2.Suggested daily plan
        3.food suggestions
        4.simple travel tips
        """)

place = input("Enter destination: ")
days = input("Enter number of days: ")
budget = input("Enter budget type(low/medium/high): ")

prompt = prompt_template.invoke({"place":place,"days":days,"budget":budget})

response = llm.invoke(prompt)

print(response.content)