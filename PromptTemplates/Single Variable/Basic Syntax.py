from langchain_core.prompts import PromptTemplate

prompt_template = PromptTemplate.from_template(
    template="Explain {topic} in simple terms.",
    input_variable = ['topic']
)

#result = prompt_template.invoke({"topic":"rag"})

text = prompt_template.format(topic="LangChain")

print(text)
#print(result)
