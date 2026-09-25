from langchain_core.runnables import RunnablePassthrough

chain = (RunnablePassthrough().assign(length=lambda x: len(x['text'])))

result = chain.invoke({"text":"Hello LangChain"})

print(result)