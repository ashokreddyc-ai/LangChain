from dotenv import load_dotenv
from langchain_core.runnables import RunnableParallel
from langchain_openai import ChatOpenAI
from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import ChatPromptTemplate

load_dotenv()

model = ChatOpenAI(model='gpt-4o-mini',temperature=0)

parser = StrOutputParser()

sentiment_prompt = ChatPromptTemplate.from_template(
    """
    Analye the sentiment of the customer review.
    review : {review}
    return only one:
    Positive
    Negative
    Neutral
    """
)

summary_prompt = ChatPromptTemplate.from_template(
    """
    summarize this customer review in one sentence.
    review:{review}
    """
)

issue_prompt = ChatPromptTemplate.from_template(
    """
    Identify the main issue mentioned by the customer.
    review:{review}
    return only the main issue
    """
)

sentiment_chain = sentiment_prompt | model | parser
summary_chain = summary_prompt | model | parser
issue_chain = issue_prompt | model | parser

parallel_chain = RunnableParallel(
                sentiment = sentiment_chain,
                summary = sentiment_chain,
                main_issue = issue_chain)

input_data = input("Enter your review : ")
# sample input : The product is excellent and the quality is very good, but the delivery was extremely slow and took two weeks.
result = parallel_chain.invoke({"review":input_data})

print("\n===== SENTIMENT =====")
print(result["sentiment"])

print("\n===== SUMMARY =====")
print(result["summary"])

print("\n===== MAIN ISSUE =====")
print(result["main_issue"])