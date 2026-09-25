from langchain_core.runnables import RunnablePassthrough

runnable = RunnablePassthrough()

result  = runnable.invoke("Hello")

print(result)