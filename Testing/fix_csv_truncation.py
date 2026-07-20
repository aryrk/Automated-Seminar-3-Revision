import csv
from run_template_coverage_FINAL import scenarios

csv_path = "/workspace/Template_Coverage_Cases_FINAL.csv"

# Map id to full narasi
narasi_map = {}
for tc in scenarios:
    narasi_map[f"TC-TPL-{tc['id']}"] = tc["narasi"]

# Read existing CSV
rows = []
with open(csv_path, "r", encoding="utf-8") as f:
    reader = csv.reader(f)
    header = next(reader)
    rows.append(header)
    for row in reader:
        tc_id = row[0]
        if tc_id in narasi_map:
            row[7] = narasi_map[tc_id] # Update narasi column
        rows.append(row)

# Write back
with open(csv_path, "w", newline="", encoding="utf-8") as f:
    writer = csv.writer(f)
    writer.writerows(rows)

print("Berhasil memperbaiki narasi yang terpotong di CSV!")
