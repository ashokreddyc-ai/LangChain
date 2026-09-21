from langchain_core.runnables import RunnableLambda

def mult(x):
    return x * x

runnable = RunnableLambda(mult)

result = runnable.invoke(5)

print(result)