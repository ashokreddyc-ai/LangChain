from dotenv import load_dotenv
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables import RunnableParallel
from langchain_openai import ChatOpenAI

load_dotenv()

model = ChatOpenAI(model='gpt-4o-mini')

parser = StrOutputParser()

document = """
Our company plans to migrate the existing SQL Server environment to Azure over the next six months.

The migration team will first migrate development databases,followed by testing and production databases.

The major risks are data migration errors, application downtime, unexpected Azure costs, and lack of cloud skillswithin the current team.

The team should conduct performance testing and create a rollback plan before migrating production workloads.
"""

summary_prompt = ChatPromptTemplate.from_template(
    """
    summarize the following document in 3 sentences
    document: {document}
    """
)

key_points_prompt = ChatPromptTemplate.from_template(
    """
    Extract the 5 most important key points from this document.
    document : {document}
    """
)


risk_prompt = ChatPromptTemplate.from_template(
    """
    Identify the major risks mentioned in this document.
    document: {document}
    return them as bullent points.
    """
)

action_prompt = ChatPromptTemplate.from_template(
    """
    Identify the recomended action items from this document.
    document: {document}
    return them as bullet points
    """
)


summary_chain = summary_prompt | model | parser
key_points_chain = key_points_prompt | model | parser
risk_chain = risk_prompt | model | parser
action_chain = action_prompt | model | parser

paraller_chain = RunnableParallel(
        summary = summary_chain,
        key_points = key_points_chain,
        risks = risk_chain,
        actions = action_chain
)

result = paraller_chain.invoke({'document':document})

print("\n========== SUMMARY ==========")
print(result["summary"])

print("\n========== KEY POINTS ==========")
print(result["key_points"])

print("\n========== RISKS ==========")
print(result["risks"])

print("\n========== ACTION ITEMS ==========")
print(result["actions"])