from langchain_core.runnables import RunnableLambda

fun = lambda x:x.strip().lower()

runnable = RunnableLambda(fun)

result = runnable.invoke(" ASHOK ")

print(result)