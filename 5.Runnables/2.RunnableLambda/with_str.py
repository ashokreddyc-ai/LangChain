from langchain_core.runnables import RunnableLambda

def upper_case(text):
    return text.upper()

runnable = RunnableLambda(upper_case)

result = runnable.invoke("hello ashok")

print(result )