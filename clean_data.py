
from pathlib import Path
import pandas as pd
import arff

INPUT_FILE = Path("dataset_")
OUTPUT_FILE = Path("employee_clean.csv")
REPORT_FILE = Path("cleaning_report.txt")

# Load the original ARFF dataset
with INPUT_FILE.open("r", encoding="utf-8") as file:
    dataset = arff.load(file)

columns = [attribute[0] for attribute in dataset["attributes"]]
df = pd.DataFrame(dataset["data"], columns=columns)

# Convert numeric columns to numeric values
numeric_columns = [
    "Employee_ID", "Age", "Salary", "Experience",
    "Performance_Score", "Working_Hours",
    "Years_in_Company", "Annual_Bonus"
]

for column in numeric_columns:
    df[column] = pd.to_numeric(df[column], errors="coerce")

# Parse dates
df["Join_Date"] = pd.to_datetime(df["Join_Date"], errors="coerce")

# Standardize text fields without changing their meaning
text_columns = df.select_dtypes(include=["object"]).columns
for column in text_columns:
    df[column] = df[column].str.strip()

# Record quality issues before cleaning
missing_before = int(df.isna().sum().sum())
duplicate_rows_before = int(df.duplicated().sum())
duplicate_ids_before = int(df["Employee_ID"].duplicated().sum())

invalid_scores = (
    df["Performance_Score"].notna()
    & ~df["Performance_Score"].between(1, 5)
)
invalid_score_count = int(invalid_scores.sum())

# Mark out-of-range performance scores as missing
df.loc[invalid_scores, "Performance_Score"] = pd.NA

# Remove exact duplicate rows, if any
df = df.drop_duplicates().copy()

# Preserve missing values rather than inventing employee information
df.to_csv(OUTPUT_FILE, index=False, date_format="%Y-%m-%d")

report = [
    "EMPLOYEE DATA CLEANING REPORT",
    f"Rows in cleaned dataset: {len(df)}",
    f"Columns: {len(df.columns)}",
    f"Missing values before cleaning: {missing_before}",
    f"Exact duplicate rows before cleaning: {duplicate_rows_before}",
    f"Duplicate Employee_ID values before cleaning: {duplicate_ids_before}",
    f"Invalid Performance_Score values changed to missing: {invalid_score_count}",
    f"Missing values after cleaning: {int(df.isna().sum().sum())}",
    f"Output file: {OUTPUT_FILE}",
]

REPORT_FILE.write_text("\n".join(report), encoding="utf-8")

print("\n".join(report))
print("\nMissing values by column after cleaning:")
print(df.isna().sum()[df.isna().sum() > 0])
print(f"\nSaved cleaned data to: {OUTPUT_FILE.resolve()}")
print(f"Saved report to: {REPORT_FILE.resolve()}")
