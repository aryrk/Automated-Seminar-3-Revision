import pandas as pd

df = pd.read_excel('/workspace/Dokumen TA/seminar sidang diff.xlsx')
col1 = df.columns[1]  # seminar
col3 = df.columns[3]  # sidang

df_clean = df.dropna(subset=[col1, col3])
diff_rows = df_clean[df_clean[col1].astype(str) != df_clean[col3].astype(str)]

# Print rows 51-200 for broader pattern
for i, (_, row) in enumerate(diff_rows.iloc[50:200].iterrows()):
    s = str(row[col1])
    d = str(row[col3])
    print(f"Row {i+51}:")
    print(f"  SEM: {s[:200]}")
    print(f"  SID: {d[:200]}")
    print()
