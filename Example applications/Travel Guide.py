import os
from dotenv import load_dotenv
from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate

load_dotenv()

llm = ChatOpenAI(model="gpt-4o-mini",)

template = ChatPromptTemplate.from_messages(
    [
        (
            "system",
            "You are a helpful travel planner. "
            "Give practical and easy-to-follow plans."
        ),
        (
            "human",
            """
            Create a {days}-day travel plan for {place}.

            Budget: {budget}
            Main Interest: {interest}

            Include:
            1. Places to visit
            2. Daily schedule
            3. Food suggestions
            4. Travel tips
            """
        )
    ]
)

place = input("Enter destination: ")
days = input("Enter number of days: ")
budget = input("Enter budget: ")
interest = input("Enter main interest: ")

prompt = template.invoke(
    {
        "place": place,
        "days": days,
        "budget": budget,
        "interest": interest
    }
)

response = llm.invoke(prompt)

print("\nTravel Plan:")
print(response.content)