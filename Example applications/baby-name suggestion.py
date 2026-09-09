from dotenv import load_dotenv
from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate

load_dotenv()

llm = ChatOpenAI(model="gpt-4o-mini")

template = ChatPromptTemplate.from_messages(
    [
        (
            "system",
            "You are an Indian baby-name advisor familiar with "
            "traditional Indian naming practices."
        ),
        (
            "human",
            """
            Suggest {count} baby names using these details:

            Gender: {gender}
            Date of birth: {date_of_birth}
            Time of birth: {time_of_birth}
            Place of birth: {place_of_birth}
            Rashi: {rashi}
            Nakshatra: {nakshatra}
            Pada: {pada}
            Religion/Tradition: {tradition}
            Preferred meaning/theme: {theme}

            For each name provide:
            1. Baby name
            2. Meaning
            3. Recommended starting syllable/letter
            4. Why the name fits the provided naming preferences

            Do not claim that astrology guarantees a child's
            personality, future, or success.
            """
        )
    ]
)

gender = input("Enter gender: ")
date_of_birth = input("Enter date of birth: ")
time_of_birth = input("Enter time of birth: ")
place_of_birth = input("Enter place of birth: ")
rashi = input("Enter Rashi: ")
nakshatra = input("Enter Nakshatra: ")
pada = input("Enter Pada: ")
tradition = input("Enter religion/tradition: ")
theme = input("Enter preferred meaning/theme: ")
count = input("Enter number of names: ")

prompt = template.invoke(
    {
        "gender": gender,
        "date_of_birth": date_of_birth,
        "time_of_birth": time_of_birth,
        "place_of_birth": place_of_birth,
        "rashi": rashi,
        "nakshatra": nakshatra,
        "pada": pada,
        "tradition": tradition,
        "theme": theme,
        "count": count
    }
)

response = llm.invoke(prompt)

print("\nBaby Name Suggestions:")
print(response.content)