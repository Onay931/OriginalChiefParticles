import os

import google.generativeai as genai

# Or use `os.getenv('GOOGLE_API_KEY')` to fetch an environment variable.
GOOGLE_API_KEY = AIzaSyAd-WX03jVey3DHlaVsTNQJjfJr_7RHL-U

genai.configure(api_key=AIzaSyBMq2OKwe4TekiDNffWsHiBFEi7LZsMzcM)

for m in genai.list_models():
  if 'generateContent' in m.supported_generation_methods:
    print(m.name)

model = genai.GenerativeModel(model_name="gemini-pro")

response = model.generate_content("How do I bake a cake?")
print(response.text)

print(response.prompt_feedback)
