## Code from the openai cookbook

# file to generate batch file for passing to gpt-4o-mini
import base64
import json
import os

# Function to encode the image
def encode_image(image_path):
    with open(image_path, "rb") as image_file:
        return base64.b64encode(image_file.read()).decode("utf-8")


tasks = []
# basically we just assume the images folder is as nice as possible
directory = "./images"

transcribe_text_prompt = """
Your goal is to transcribe the given images. You will be provided with images containing Japanese text, 
that provides a word, its reading and a definition alongside example sentences. You will output a json object 
containing the following:
{
  word: string //The given word, in bold in the upper corner
  reading: string //The reading of the given word
  definition: string //The remaining text as is.
}
the "reading" refers to the hiragana characters enclosed by brackets.  
"""
# just to generate ids
i = 1


for filename in os.listdir(directory):
    if filename.endswith('.png'):
        image_path = os.path.join(directory,filename)
        base64_image = encode_image(image_path)
        
        task = {
            "custom_id": f"task-{i}",
            "method": "POST",
            "url": "/v1/chat/completions",
            "body": {
                # This is what you would have in your Chat Completions API call
                "model": "gpt-4o-mini",
                "temperature": 0.1,
                "response_format": { 
                    "type": "json_object"
                },
                "messages": [
                    {
                        "role": "system",
                        "content": transcribe_text_prompt
                    },
                    {
                        "role": "user",
                        "content": [
                            {
                                "type":"image_url",
                                "image_url": {"url": f"data:image/jpeg;base64,{base64_image}"},
                            },
                        ],
                    },
                ],
            }
        }
        # add one
        i+=1
        # append to tasks
        tasks.append(task)

# Creating the file
file_name = "batch_tasks_words.jsonl"

with open(file_name, 'w') as file:
    for obj in tasks:
        file.write(json.dumps(obj) + '\n')
