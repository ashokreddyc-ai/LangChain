from dotenv import load_dotenv
from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables import RunnableParallel

load_dotenv()

model = ChatOpenAI(model='gpt-4o-mini',temperature=0)

parser = StrOutputParser()

simple_prompt =ChatPromptTemplate.from_template(""" 
        Explain {topic} in very simple english.
        Assume the reader is beginner.
        Keep it with in 5 sentences.
        """)

technical_prompt = ChatPromptTemplate.from_template("""
        Explain {topic} from technical perspective.
        use appropriate technical terminology.
        keep it within 5 sentence        
        """)

example_prompt = ChatPromptTemplate.from_template("""
        Give one practical real-world example of {topic}.
        Explain the example clearly.
        """)


simple_chain = simple_prompt | model | parser
technical_chain = technical_prompt | model | parser
example_chain = example_prompt | model | parser

parallel_chain = RunnableParallel(
    simple = simple_chain,
    technical = technical_chain,
    example = example_chain
)

input_data = input("Enter Required topic: ")

result = parallel_chain.invoke({"topic":input_data})

print("\n===== SIMPLE EXPLANATION =====")
print(result["simple"])

print("\n===== TECHNICAL EXPLANATION =====")
print(result["technical"])

print("\n===== REAL-WORLD EXAMPLE =====")
print(result["example"])