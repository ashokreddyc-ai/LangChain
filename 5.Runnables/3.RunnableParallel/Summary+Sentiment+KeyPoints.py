from dotenv import load_dotenv
from langchain_core.runnables import RunnableParallel
from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import ChatPromptTemplate
from langchain_openai import ChatOpenAI

load_dotenv()

llm = ChatOpenAI(model='gpt-4o-mini',temperature=0)

parser = StrOutputParser()

summary_prompt = ChatPromptTemplate.from_template("Summarize this text in 2 sentences: \n{text}")

sentiment_prompt = ChatPromptTemplate.from_template("Analyze the sentiment of this text:\n{text}")

key_points_prompt = ChatPromptTemplate.from_template("Extract 3 key points from this text:\n{text}")

summary_chain = summary_prompt | llm | parser
sentiment_chain  = sentiment_prompt | llm | parser
key_points_chain = key_points_prompt | llm | parser


parallel_chain = RunnableParallel(
        summary = summary_chain,
        sentiment = sentiment_chain,
        key_points = key_points_chain
)

result = parallel_chain.invoke({"text": "The payment failed several times and the customer is frustrated."})

print(result)
