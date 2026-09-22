from langchain_core.runnables import RunnableLambda,RunnableParallel

runnable1_square = RunnableLambda(lambda x:x*x)
runnable1_cube = RunnableLambda(lambda x:x*x*x)

parallel = RunnableParallel(square=runnable1_square,
                            cube = runnable1_cube)

result = parallel.invoke(5)
print(result)