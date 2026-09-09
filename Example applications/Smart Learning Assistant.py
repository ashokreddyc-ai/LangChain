import os
from dotenv import load_dotenv
from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate

llm = ChatOpenAI(
    model="gpt-4o-mini",
)

template = ChatPromptTemplate.from_messages(
    [
        (
            "system",
            """
            You are an expert {subject} teacher.

            Student Level: {level}
            Language: {language}
            Teaching Style: {style}

            Always make the explanation
            easy to understand.
            """
        ),
        (
            "human",
            """
            Teach me {topic}.

            Give:
            1. A simple definition
            2. Why it is required
            3. Important points
            4. {examples} simple examples
            5. One common mistake
            6. One-line conclusion
            """
        )
    ]
)

subject = input("Enter subject: ")
topic = input("Enter topic: ")
level = input("Enter student level: ")
language = input("Enter language: ")
style = input("Enter teaching style: ")
examples = input("How many examples?: ")

prompt = template.invoke(
    {
        "subject": subject,
        "topic": topic,
        "level": level,
        "language": language,
        "style": style,
        "examples": examples
    }
)


response = llm.invoke(prompt)

print("\n========== AI RESPONSE ==========")
print(response.content)