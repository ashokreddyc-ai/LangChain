from langchain_core.runnables import RunnableParallel,RunnableLambda

add = RunnableLambda(lambda x:x+10)
mul = RunnableLambda(lambda x:x*10)
sqr = RunnableLambda(lambda x:x*2)

parallel = RunnableParallel(add = add,
                            mul = mul,
                            sqr = sqr)

result = parallel.invoke(5)
print(result)

