import json
from openai import OpenAI

# load api key
with open ('config.json') as config:
    data = json.load(config)

client = OpenAI(api_key=data['api_key'])

# just really basic code to figure out the batch id
#print(client.files.list())

result = client.files.content("file-Bd1mfeGvpZvmDr4SJ6eNEV").content
result_file_name = "results/batch_job_results_words.jsonl"

with open(result_file_name, 'wb') as file:
    file.write(result)


#result_file_id = batch_job.output_file_id
#result = client.files.content(result_file_id).content

#for res in results:
#    print(res)
    #result = res['response']['body']['choices'][0]['message']['content']
    #print(f"RESULT: {result}")
    #print("\n\n----------------------------\n\n")