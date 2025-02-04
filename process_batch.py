import json 
import ast
dicts = []
results = []

result_file_name = "results/batch_job_results_words.jsonl"
output_file_name = "results/batch_job_cleaned_output.jsonl"

with open(result_file_name, 'r') as file:
    for line in file:
        # Parsing the JSON string into a dict and appending to the list of results
        json_object = json.loads(line.strip())
        results.append(json_object)

for res in results:
    # result is basically a dixt
    result = res['response']['body']['choices'][0]['message']['content']
    dict = ast.literal_eval(result)

    dicts.append(dict)

# back to json
json_output = json.dumps(dicts,ensure_ascii=False,indent=2)
print(json_output)

with open(output_file_name,"w") as outfile:
    outfile.write(json_output)