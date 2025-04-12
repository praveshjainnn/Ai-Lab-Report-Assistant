from flask import Flask, request, jsonify
from flask_cors import CORS
import os
from dotenv import load_dotenv
import openai

load_dotenv()

app = Flask(__name__)
CORS(app)

# Check if API key is available
api_key = os.getenv("OPENROUTER_API_KEY")
if not api_key:
    raise ValueError("OPENROUTER_API_KEY not found in environment variables. Please add it to your .env file.")

# Set OpenRouter API config
client = openai.OpenAI(
    api_key=api_key,
    base_url="https://openrouter.ai/api/v1"
)

# Set default headers for OpenRouter
openai.default_headers = {
    "HTTP-Referer": "http://localhost:5000",
    "X-Title": "AI Lab Report Assistant"
}

@app.route("/generate", methods=["POST"])
def generate():
    try:
        data = request.get_json()
        if not data:
            return jsonify({"error": "No data provided"}), 400
            
        prompt = data.get("prompt")
        if not prompt:
            return jsonify({"error": "No prompt provided"}), 400

        print(f"Sending prompt to OpenRouter: {prompt}")  # Debug log

        response = client.chat.completions.create(
            model="mistralai/mistral-7b-instruct",
            messages=[
                {"role": "system", "content": "You are a helpful AI lab report assistant. Generate detailed, well-structured lab reports."},
                {"role": "user", "content": prompt}
            ],
            temperature=0.7,
            max_tokens=2000
        )

        if not response or not response.choices:
            return jsonify({"error": "No response from AI model"}), 500

        generated_text = response.choices[0].message.content
        print(f"Received response from OpenRouter: {generated_text[:100]}...")  # Debug log

        return jsonify({"response": generated_text})

    except openai.APIError as e:
        print(f"OpenRouter API Error: {str(e)}")
        return jsonify({"error": "API Error: " + str(e)}), 500
    except Exception as e:
        print(f"Unexpected Error: {str(e)}")
        return jsonify({"error": "Failed to generate report. Please try again."}), 500

@app.route("/health", methods=["GET"])
def health_check():
    return jsonify({"status": "healthy", "api_key_configured": bool(api_key)}), 200

if __name__ == "__main__":
    print("Starting Flask server...")
    print(f"API Key configured: {'Yes' if api_key else 'No'}")
    app.run(debug=True, host='127.0.0.1', port=5000)
