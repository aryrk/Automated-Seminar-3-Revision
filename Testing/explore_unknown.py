import pandas as pd

df = pd.read_csv('/workspace/Testing/NLP_Validation_Cases.csv')
print(df[df['Test Type (MFT/INV/DIR)'] == 'UNKNOWN']['Test Case Name* (Scenario)'])

# Let's fix MFT/DIR to either MFT or DIR based on exact count and what it is.
# Table says Relevansi dan cakupan is 21 cases (MFT & DIR)
# Let's see what is unknown
