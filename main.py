from langchain_ollama import OllamaLLM
from langchain_core.prompts import ChatPromptTemplate

model = OllamaLLM(model="qwen2.5:3b")

template="""
You are an expert for answering questions for a pizza restaurant

Here are some relevant reviews: {reviews}

Here is the question: {question}

"""
prompt = ChatPromptTemplate.from_template(template)
chain  = prompt | model

result = chain.invoke({"reviews": [], "question":"What is the best pizza place in town?"})
print(result)