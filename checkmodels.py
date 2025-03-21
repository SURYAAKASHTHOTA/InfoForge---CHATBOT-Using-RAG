import google.generativeai as genai

genai.configure(api_key="AIzaSyATaiSlm5NzV_nXBlufw9ZPgeAcmE8wEnA")  # Replace with your actual API key

models = genai.list_models()
for model in models:
    print(model.name)
