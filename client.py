# from openai import OpenAI
# # client = OpenAI()
# # pip install OpenAi
# client = OpenAI(
#     api_key = "<api key>"
#     # api_key = os.environ.get("CUSTOM_ENV_NAME"),
# )
# completion = client.chat.completions.create(
#     model="gpt-4o-mini",
#     messages=[
#         {"role": "system", "content": "You are a virtual assistant named jarvis skilled in general tasks like Alexa and Google Cloud."},
#         {
#             "role": "user",
#             "content": "which is best programming language"
#         }
#     ]
# )

# print(completion.choices[0].message.content)

# need api key (paid)