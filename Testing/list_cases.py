import pandas as pd

df = pd.read_csv('/workspace/Testing/NLP_Validation_Cases.csv')

# Helper to print test case names for manual categorization
cases = df['Test Case Name* (Scenario)'].tolist()
for c in cases:
    print(c)
