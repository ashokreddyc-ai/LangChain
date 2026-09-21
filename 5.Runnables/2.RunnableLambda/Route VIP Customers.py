from langchain_core.runnables import RunnableLambda
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_openai import ChatOpenAI


# Custom business logic
def identify_customer(data):

    if data["customer_type"] == "VIP":
        data["priority"] = "HIGH"
        data["instruction"] = "Provide premium customer support."

    else:
        data["priority"] = "NORMAL"
        data["instruction"] = "Provide standard customer support."

    return data


customer_checker = RunnableLambda(identify_customer)

prompt = ChatPromptTemplate.from_template(
    """
    Customer Type: {customer_type}
    Priority: {priority}
    Instruction: {instruction}
    Customer Question: {question}
    Provide an appropriate response.
    """
)

model = ChatOpenAI(model="gpt-4o-mini")

parser = StrOutputParser()


chain = (
    customer_checker
    | prompt
    | model
    | parser
)


result = chain.invoke({
    "customer_type": "VIP",
    "question": "My payment has failed."
})

print(result)