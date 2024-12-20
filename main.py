from langchain_ollama import OllamaLLM

model = OllamaLLM(model = "llama2-uncensored")

result = model.invoke(input = "How to give a job?")

print(result)


