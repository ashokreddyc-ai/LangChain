from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.runnables import RunnableParallel
from dotenv import load_dotenv
from langchain_core.output_parsers import StrOutputParser

load_dotenv()

llm = ChatOpenAI(model="gpt-4o-mini",temperature=0)

review = """
The laptop has excellent performance and very good battery life. However, the keyboard feels uncomfortable for long working sessions and the price is quite high.
"""

sentiment_prompt = ChatPromptTemplate.from_template(
    """
    Analyze the sentiment of this review.

    Review:
    {review}

    Return:
    Overall sentiment
    and a short explanation.
    """
)


pros_prompt = ChatPromptTemplate.from_template(
    """
    Extract the positive aspects of this product review.

    Review:
    {review}

    Return the positive aspects as bullet points.
    """
)


cons_prompt = ChatPromptTemplate.from_template(
    """
    Extract the negative aspects of this product review.

    Review:
    {review}

    Return the negative aspects as bullet points.
    """
)


reasoning_prompt = ChatPromptTemplate.from_template(
    """
    Analyze what factors a customer should consider
    before purchasing this product based on the review.

    Review:
    {review}

    Do not make the final buying decision.
    Just explain the relevant considerations.
    """
)

parser = StrOutputParser()

sentiment_chain = sentiment_prompt | llm | parser

pros_chain = pros_prompt | llm | parser

cons_chain = cons_prompt | llm | parser

reasoning_chain = reasoning_prompt | llm | parser


parallel_chain = RunnableParallel(
    sentiment=sentiment_chain,
    pros=pros_chain,
    cons=cons_chain,
    considerations=reasoning_chain
)


final_prompt = ChatPromptTemplate.from_template(
    """
    You are a product analysis assistant.

    Create a concise product analysis using the
    following independent analyses.

    SENTIMENT:
    {sentiment}

    PROS:
    {pros}

    CONS:
    {cons}

    CONSIDERATIONS:
    {considerations}

    Format your answer exactly as:

    Overall Sentiment:
    <answer>

    Pros:
    <bullet points>

    Cons:
    <bullet points>

    Important Considerations:
    <bullet points>
    """
)

final_chain = final_prompt | llm | parser

complete_chain = (parallel_chain | final_chain)


result = complete_chain.invoke({"review": review})


print("\n===================================")
print("       PRODUCT ANALYSIS")
print("===================================\n")

print(result)