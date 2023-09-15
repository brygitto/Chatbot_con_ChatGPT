import openai

# Indica el API KEY
openai.api_key = "sk-yqj8VavOD2ZRet0HlbB4T3BlbkFJaxXKS8Ns2s121524a"

# Uso de ChatGPT en PYTHON
model_engine = "text-davinci-003"
prompt = "que comida es la mejor para los perros"
completion = openai.Completion.create(engine=model_engine, prompt=prompt, max_tokens=1024, n=1, stop=None, temperature=0.7)
respuesta = ""
for choice in completion.choices:
    respuesta = respuesta + choice.text
    print(f"Response: %s" % choice.text)
