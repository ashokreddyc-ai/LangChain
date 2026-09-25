from langchain_core.runnables import (RunnablePassthrough,RunnableParallel)


chain = RunnableParallel(
    original_input=RunnablePassthrough(),
    message=lambda x: f"Received: {x}"
)

result = chain.invoke("What is LangChain?")


print(result)