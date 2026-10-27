
from pathlib import Path
import pandas as pd
import arff

file_path = Path("dataset_")

print("Reading dataset...")

with file_path.open("r", encoding="utf-8") as file:
    dataset = arff.load(file)

columns = [attribute[0] for attribute in dataset["attributes"]]
df = pd.DataFrame(dataset["data"], columns=columns)

print("\n--- DATASET OVERVIEW ---")
print(f"Rows: {df.shape[0]:,}")
print(f"Columns: {df.shape[1]}")

print("\n--- COLUMN NAMES ---")
print(df.columns.tolist())

print("\n--- DATA TYPES ---")
print(df.dtypes)

print("\n--- MISSING VALUES ---")
print(df.isnull().sum().sort_values(ascending=False))

print("\n--- DUPLICATE ROWS ---")
print(df.duplicated().sum())

print("\n--- SAMPLE DATA ---")
print(df.head())

print("\n--- NUMERIC SUMMARY ---")
print(df.describe().T)

print("\n--- DATA QUALITY CHECKS ---")

checks = {
    "Duplicate Employee_IDs": df["Employee_ID"].duplicated().sum(),
    "Age below 18 or above 100": (
        (df["Age"] < 18) | (df["Age"] > 100)
    ).sum(),
    "Negative Salary": (df["Salary"] < 0).sum(),
    "Negative Experience": (df["Experience"] < 0).sum(),
    "Negative Working_Hours": (df["Working_Hours"] < 0).sum(),
    "Performance_Score below 1 or above 5": (
        (df["Performance_Score"] < 1)
        | (df["Performance_Score"] > 5)
    ).sum(),
    "Years in Company greater than Experience": (
        df["Years_in_Company"] > df["Experience"]
    ).sum(),
}

for check, count in checks.items():
    print(f"{check}: {count}")

print("\n--- PERFORMANCE SCORE VALUES ---")
print(df["Performance_Score"].value_counts(dropna=False).sort_index())

print("\n--- DATE VALIDATION ---")
dates = pd.to_datetime(df["Join_Date"], errors="coerce")
print(f"Invalid Join_Date values: {dates.isna().sum()}")
print(f"Earliest Join_Date: {dates.min()}")
print(f"Latest Join_Date: {dates.max()}")

print("\n--- INVALID PERFORMANCE SCORE RECORDS ---")
invalid_scores = df[
    df["Performance_Score"].notna()
    & ~df["Performance_Score"].between(1, 5)
]
print(invalid_scores[
    ["Employee_ID", "Age", "Performance_Score", "Department"]
].head(15))
print(f"Total invalid scores: {len(invalid_scores)}")

print("\n--- CATEGORICAL VALUES ---")
for column in [
    "Gender", "Department", "Education", "Country"
]:
    print(f"\n{column}:")
    print(df[column].value_counts(dropna=False).head(15))

print("\n--- EXPERIENCE AND TENURE CHECK ---")
print("Experience maximum:", df["Experience"].max())
print("Years in company maximum:", df["Years_in_Company"].max())

