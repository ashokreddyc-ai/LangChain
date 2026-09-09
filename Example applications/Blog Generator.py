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
            "You are a professional content writer."
        ),
        (
            "human",
            """
            Write a blog on {topic}.

            Target Audience: {audience}
            Tone: {tone}
            Length: approximately {length}

            Include:
            - Attractive title
            - Introduction
            - Main sections
            - Useful examples
            - Conclusion
            """
        )
    ]
)

topic = input("Enter blog topic: ")
audience = input("Enter audience: ")
tone = input("Enter tone: ")
length = input("Enter approximate length: ")

prompt = template.invoke(
    {
        "topic": topic,
        "audience": audience,
        "tone": tone,
        "length": length
    }
)

response = llm.invoke(prompt)

print("\nGenerated Blog:")
print(response.content)