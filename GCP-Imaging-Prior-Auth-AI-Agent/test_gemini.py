from vertexai.preview.generative_models import GenerativeModel
import vertexai

vertexai.init(project="weighty-nation-463615-h5", location="us-central1")

model = GenerativeModel("gemini-pro")
response = model.generate_content("Summarize this: A 52-year-old female underwent an MRI scan...")
print(response.text)

