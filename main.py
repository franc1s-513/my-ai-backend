import os
from flask import Flask, request, jsonify
from flask_cors import CORS
from dotenv import load_dotenv
import google.generativeai as genai

# 1. Load environment variables
load_dotenv()

app = Flask(__name__)
CORS(app) # This prevents the "CORS error" on Vercel

# 2. Get the Secret Key from Render
api_key = os.getenv("API_KEY")

# 3. THE DETECTIVE LINE (Check your Render Logs for this!)
if api_key:
    print(f"DEBUG: API_KEY successfully loaded. Starts with: {api_key[:5]}...")
else:
    print("DEBUG: ERROR - API_KEY not found in Environment Variables!")

# 4. Configure Gemini
genai.configure(api_key=api_key)
model = genai.GenerativeModel('gemini-1.5-flash')

@app.route('/')
def home():
    return "AI Backend is Running!"

@app.route('/chat', methods=['GET'])
def chat():
    user_message = request.args.get('message')
    
    if not user_message:
        return jsonify({"reply": "I didn't hear anything! What's on your mind?"})

    try:
        # Generate the response
        response = model.generate_content(user_message)
        
        # Return as 'reply' to match your React code
        return jsonify({"reply": response.text})
        
    except Exception as e:
        print(f"Chat Error: {e}")
        return jsonify({"reply": "My brain is a bit foggy. Check the API key in Render!"})

if __name__ == '__main__':
    # Render uses the PORT environment variable
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)