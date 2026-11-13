from langchain_ollama import OllamaLLM
from langchain_core.prompts import ChatPromptTemplate
from vector import retriever

model = OllamaLLM(model="qwen2.5:3b")

template="""
You are an expert for answering questions for a pizza restaurant

Here are some relevant reviews: {reviews}

Here is the question: {question}

"""
prompt = ChatPromptTemplate.from_template(template)
chain  = prompt | model

while(True):
    print("-----------------------------------------------------")
    question = input("Ask your question (q to quit): ")
    print("-----------------------------------------------------")
    if question == "q":
        break

    reviews = retriever.invoke(question)
    result = chain.invoke({"reviews": reviews, "question":question})
    print(result)