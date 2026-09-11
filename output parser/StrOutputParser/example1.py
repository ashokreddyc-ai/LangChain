from dotenv import load_dotenv
from langchain_openai.chat_models import ChatOpenAI

load_dotenv()

llm = ChatOpenAI(model="gpt-4o-mini")

response = llm.invoke("what is python? explain in one sentence")

# print(type(response))

# print("#####response#####")
# print(response)

print("input tokens: ",response.usage_metadata['input_tokens'])
print("input tokens: ",response.usage_metadata['input_token_details'])

print("output tokens: ",response.usage_metadata['output_tokens'])
print("output tokens: ",response.usage_metadata['output_token_details'])

print("output tokens: ",response.usage_metadata['total_tokens'])

print("Model provider: ",response.response_metadata['model_provider'])

print("Model provider: ",response.response_metadata['model_name'])