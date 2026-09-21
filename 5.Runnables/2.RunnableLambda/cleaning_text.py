from langchain_core.runnables import RunnableLambda

def clean_text(text):
    return text.strip().lower()

cleaner = RunnableLambda(clean_text)

response = cleaner.invoke(" HELLO WORLD")

print(response)