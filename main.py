import base64
import json
from openai import OpenAI

# load api key
with open ('config.json') as config:
    data = json.load(config)

client = OpenAI(api_key=data['api_key'])

batch_file = client.files.create(
    file=open('batch_tasks_words.jsonl','rb'),
    purpose='batch'
)
print(batch_file)

batch_job = client.batches.create(
  input_file_id=batch_file.id,
  endpoint="/v1/chat/completions",
  completion_window="24h"
)