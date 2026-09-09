from dotenv import load_dotenv
from langchain_openai.chat_models import ChatOpenAI
from langchain_core.messages import HumanMessage,AIMessage,SystemMessage
from langchain_core.prompts import PromptTemplate,ChatPromptTemplate

load_dotenv()

llm = ChatOpenAI(model="gpt-4o-mini")

template = ChatPromptTemplate.from_messages(
    [
        ('system','you are a creative branding expert who creates restaurant names.'),
        ('human',""" suggest 10 restaurant names 
        cuisine : {cuisine}
        location : {location}
        style : {style}
        """)
    ]
)

cuisine =input("Enter cuisine: ")
location = input("Enter location: ")
style = input("Enter style: ")

prompt = template.invoke({"cuisine":cuisine,"location":location,"style":style})

response = llm.invoke(prompt)

print(response.content)
