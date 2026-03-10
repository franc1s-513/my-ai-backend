import google.generativeai as genai

# 1. Setup (Put your key here)
genai.configure(api_key="AIzaSyB_FljPIEavPpSV2OlAVyT6OPuMy_liDoQ")

# 2. Pick the NEW 2026 model
model = genai.GenerativeModel('gemini-3-flash-preview')

# 3. This is your "Training Data" (The Knowledge Base)
my_data = """
Project Name: DragonChat 2026.
Owner: A 2nd-year CSE student.
Special Rule: Always end every reply with the word 'ROAR!'.
Favorite Language: Python.
"""

# 4. We combine your data + the user's question
user_question = "What is your favorite language and who owns you?"

prompt = f"Use this info: {my_data}. Question: {user_question}"

# 5. Get the response
response = model.generate_content(prompt)

print("--- BOT RESPONSE ---")
print(response.text)