from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain_openai.chat_models import ChatOpenAI


load_dotenv()

llm = ChatOpenAI(model="gpt-4o-mini")

template = PromptTemplate.from_template(
        """
    Explain {topic} to a beginner.
  Use:
    - Very simple English
    - 5 important points
    - One real-life example
    """
)

topic = input("Enter topic: ")

promt = template.invoke({"topic":topic}) # To extract prompt from tempalate 

result = llm.invoke(promt) # Sending prompt to llm

print(result.content)