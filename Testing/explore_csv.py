import pandas as pd

df = pd.read_csv('/workspace/Testing/NLP_Validation_Cases.csv')
print(df[['Test Case ID', 'Test Case Name* (Scenario)']].head(20))
print("Total rows:", len(df))
