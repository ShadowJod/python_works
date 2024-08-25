from openai import OpenAI

client = OpenAI(api_key = "sk-KgLue2fFcJnxn6h8u6nw3MYEt3kmVBELLmu37StKiBT3BlbkFJzGadNnF2FGUQGoJ7M-bVRRA1i28Qfra5AshvqvFw4A")


completion = client.chat.completions.create(
  model="GPT-3.5 Turbo",
  messages=[
    {"role": "system", "content": "You are a poetic assistant, skilled in explaining complex programming concepts with creative flair."},
    {"role": "user", "content": "What is python."}
  ]
)

# print(completion.choices[0].message)
print(completion)
