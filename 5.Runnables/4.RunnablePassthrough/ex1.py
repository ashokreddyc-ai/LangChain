from langchain_core.runnables import (RunnableLambda,RunnableParallel,RunnablePassthrough)

double = RunnableLambda(lambda x:x*2)
square = RunnableLambda(lambda x:x*x)

parallel = RunnableParallel(
    original = RunnablePassthrough(),
    double = double,
    square = square
)

result = parallel.invoke(5)

print(result)
print(result["double"])
print(result['square'])
print(result['original'])