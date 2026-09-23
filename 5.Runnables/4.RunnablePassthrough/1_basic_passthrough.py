from langchain_core.runnables import RunnablePassthrough

passthrough = RunnablePassthrough()

input_data = input("Enter required topic: ")

result = passthrough.invoke(input=input_data)

print("Input :", input_data)
print("Output:", result)