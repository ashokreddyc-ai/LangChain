from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain_openai import ChatOpenAI
from langchain_core.output_parsers import StrOutputParser

load_dotenv()

model = ChatOpenAI(model="gpt-4o-mini")

prompt = PromptTemplate.from_template(""" create a {days}-days travel plan for {place}.
    budget: {budget}
    main interest {interest}
    keep the plan simple
""")

parser =  StrOutputParser()

chain = prompt | model | parser

days = input("Enter number is days: ")
place = input("Enter planed place to visit: ")
budget = input("Enter your budget: ")
interest = input("Enter your intersets in above entered place: ")

result = chain.invoke({"days":days,"place":place,"budget":budget,"interest":interest})

print(result)