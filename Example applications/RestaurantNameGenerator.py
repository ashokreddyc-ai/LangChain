from dotenv import load_dotenv
from langchain_openai.chat_models import ChatOpenAI
from langchain_core.messages import HumanMessage,AIMessage,SystemMessage
from langchain_core.prompts import PromptTemplate,ChatPromptTemplate

load_dotenv()

llm = ChatOpenAI(model="gpt-4o-mini")

template = PromptTemplate.from_template(
    """
    Suggest 10 restaurant names.
    cuisine: {cuisine}
    location: {location}
    style: {style}

    The name should be:
    1.attractive
    2.Easy to remember
    3.suitable for the cuisine
    """
)

cuisine =input("Enter cuisine: ")
location = input("Enter location: ")
style = input("Enter style: ")

prompt = template.invoke({"cuisine":cuisine,"location":location,"style":style})

response = llm.invoke(prompt)

print(response.content)
