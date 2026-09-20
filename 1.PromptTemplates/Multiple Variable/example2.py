from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain_openai.chat_models import ChatOpenAI

load_dotenv()

llm = ChatOpenAI(model="gpt-4o-mini")

prompt_template = PromptTemplate.from_template(
    """
    Teach me {topic}.
    Student Level: {level}
    Language : {language}
    Explanation style: {style}

    Requirements:
    1.Explain in easy langauge
    2.Give 5 important points
    3.Give 2 real life example
    4.metion one common mistake
    5.End with aone-line conclusion
    """
)

topic = input("Enter topic:")
level = input("Enter your level: ")
language = input("Enter Language: ")
style = input("Enter Explanation style: ")


prompt = prompt_template.invoke(
    {"topic":topic,"level":level,"language":language,"style":style}
)

respone = llm.invoke(prompt)
print(respone.content)