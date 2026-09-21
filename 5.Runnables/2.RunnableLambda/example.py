from dotenv import load_dotenv
from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables import RunnableLambda

load_dotenv()

model =ChatOpenAI(model="gpt-4o-mini",temperature=0)

parser = StrOutputParser()

prompt1 = ChatPromptTemplate.from_template("""
        Explain {topic} in simple english.
        give a simple definition and 5 important points
        """)

to_dict = RunnableLambda(lambda explanation:{"explanation":explanation})

prompt2 = ChatPromptTemplate.from_template("""
        Based on the explanation below, create 5 beginner interview questions.
        Explanation: {explanation}
        """)

chain = (prompt1 | model | parser | to_dict | prompt2 | model | parser)

result = chain.invoke({"topic":"python"})

print(result)