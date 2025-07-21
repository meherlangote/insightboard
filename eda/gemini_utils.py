import google.generativeai as genai

# Setup Gemini API (Free API from Google AI Studio)
genai.configure(api_key="YOUR_GEMINI_API_KEY")

# Create model
model = genai.GenerativeModel("gemini-pro")

def generate_insight(prompt: str) -> str:
    try:
        response = model.generate_content(prompt)
        return response.text
    except Exception as e:
        return f"❌ Error generating insight: {str(e)}"
