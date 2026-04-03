import json

def fix_notebook_json(filename):
    with open(filename, 'r', encoding='utf-8') as f:
        data = json.load(f)
    
    # Check if the 'widgets' key exists in notebook metadata
    if 'metadata' in data and 'widgets' in data['metadata']:
        del data['metadata']['widgets']
        print(f"Removed corrupted widget metadata from {filename}")
        
        with open(filename, 'w', encoding='utf-8') as f:
            json.dump(data, f, indent=1) # indent=1 keeps the file readable
    else:
        print("No widget metadata found.")

fix_notebook_json("CnnsRecognition.ipynb")