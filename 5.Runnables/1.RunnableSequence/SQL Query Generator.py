from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_openai import ChatOpenAI
from langchain_core.runnables import RunnableSequence


# 1. Prompt
prompt = ChatPromptTemplate.from_template(
    """
    You are an expert SQL developer.

    Convert the user's question into Microsoft SQL Server SQL.

    Database schema:

    customers(
        customer_id,
        customer_name,
        city,
        signup_date
    )

    transactions(
        transaction_id,
        customer_id,
        amount,
        transaction_date,
        status
    )

    User question:
    {question}

    Rules:
    - Generate only SQL.
    - Use Microsoft SQL Server syntax.
    - Do not explain the query.
    """
)


# 2. Model
model = ChatOpenAI(
    model="gpt-4o-mini",
    temperature=0
)


# 3. Parser
parser = StrOutputParser()


# 4. RunnableSequence
sql_chain = RunnableSequence(
    prompt,
    model,
    parser
)


# 5. User question
question = """
Show the top 10 customers based on
their total successful transaction amount.
"""


# 6. Execute
sql_query = sql_chain.invoke({
    "question": question
})


print("Generated SQL:")
print(sql_query)