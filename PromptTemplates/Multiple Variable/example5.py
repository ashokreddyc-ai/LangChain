from dotenv import load_dotenv
from langchain_openai.chat_models import ChatOpenAI
from langchain_core.prompts import PromptTemplate

load_dotenv()

llm = ChatOpenAI(model="gpt-4o-mini")

prompt_template = PromptTemplate(
    """
    Suggest 10 restaurant names.
    cuisine: {cuisine}
    style : {style}
    location: {location}

    name shoudl be:
    1.Easy to remember
    2.Attractive
    3.Suitable for the restaurant
    """
)

cuisine = input("Enter cuisine: ")
style = input("Enter your style: ")
location = input("Enter required location: ")

prompt = prompt_template.invoke({"cuisine":cuisine,"style":style,"location":location})

response = llm.invoke(prompt)

print(response.content)