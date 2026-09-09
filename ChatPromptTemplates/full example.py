from dotenv import load_dotenv
from langchain_core.messages import HumanMessage,AIMessage,SystemMessage
from langchain_core.prompts import ChatPromptTemplate
from langchain_openai.chat_models import ChatOpenAI

load_dotenv()

llm = ChatOpenAI(model='gpt-4o-mini')

template = ChatPromptTemplate.from_messages([
    (
        "system",
        """
        you are an expert {subject} teacher.
        subject Level: {level}
        Language: {Language}
        your job is teach concepts clearly and use easy examples.
        """
    ),
    (
        "human",
        """
        Teach me {topic}.
        requirements:
        1.Give a simple definition.
        2.Explain why it required.
        3.give 5 important points.
        4.give 3 real life example.
        5.mention common mistakes.
        6.end with one line conclusion
        """
    )]
)

subject = input("Enter subject: ")
level = input("Enter Level: ")
Language = input("Enter Language: ")
topic = input("Enter topic: ")

prompt = template.invoke({
    "subject":subject,
    "level" : level,
    "Language" : Language,
    "topic" : topic 
})

response = llm.invoke(prompt)
print(response.content)