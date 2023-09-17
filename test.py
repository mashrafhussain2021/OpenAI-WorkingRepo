import openai
import os

deployment_name = "SampleModel"
openai.api_type = "azure"
#openai.api_key = os.getenv("OPENAI_API_KEY")
openai.api_key = "c8bd709bb22d420a845b1ba3140bc326"
openai.api_base = "https://azureaipilotinstance.openai.azure.com/"
openai.api_version = "2022-12-01"


prompt = input("What do you want to know ....")

result = openai.Completion.create(
  engine=deployment_name,
  prompt=prompt,
  temperature=0.2,
  max_tokens=150
)

result.choices[0].text.strip(" \n")
print(result.choices[0].text.strip(" \n"))
