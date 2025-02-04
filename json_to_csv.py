import pandas as pd

frame = pd.read_json('results/batch_job_cleaned_output.jsonl')
frame['reading'] = frame['reading'].apply(lambda x: f'[{x}]')
# this is to get it to work well with the furigana display 
frame['reading']=frame['word']+frame['reading']

# now we just export as csv
frame.to_csv('results/output.csv')