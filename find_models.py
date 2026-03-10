import google.generativeai as genai

# Replace with your actual key
genai.configure(api_key="AIzaSyB_FljPIEavPpSV2OlAVyT6OPuMy_liDoQE")

print("Checking available models...")
for m in genai.list_models():
    if 'generateContent' in m.supported_generation_methods:
        print(f"- {m.name}")