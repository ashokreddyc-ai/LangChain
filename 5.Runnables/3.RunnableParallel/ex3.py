from langchain_core.runnables import RunnableParallel,RunnableLambda

retrieve_docs = RunnableLambda(lambda query:f"documents related to {query}")

detect_sentiment = RunnableLambda(lambda query: "Negative")

classify_query = RunnableLambda(lambda query: "Payment Declined")

parallel = RunnableParallel(documents = retrieve_docs,
                            sentiment=detect_sentiment,
                            category=classify_query)

result = parallel.invoke("Why was my payment in sucess?")

print(result)