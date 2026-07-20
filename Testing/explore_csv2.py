import pandas as pd
import json

df = pd.read_csv('/workspace/Testing/NLP_Validation_Cases.csv')

# Extract prefixes and analyze counts
groups = {}
for name in df['Test Case Name* (Scenario)'].fillna(''):
    if '—' in name:
        prefix = name.split('—')[0].strip()
    elif '-' in name:
         prefix = name.split('-')[0].strip()
    else:
        prefix = name.split(' ')[0].strip()
    
    groups[prefix] = groups.get(prefix, 0) + 1

print(json.dumps(groups, indent=2))
