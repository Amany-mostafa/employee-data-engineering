# Employee Data Engineering Project

I built this project to practice working with employee data using Python and SQL Server.

The project starts with a raw dataset, checks data quality issues, cleans the data using Pandas, and loads the result into SQL Server. I then used SQL queries to check the loaded data and explore employee and salary information.

## Tools Used

- Python
- Pandas
- SQLAlchemy
- pyodbc
- Microsoft SQL Server
- SQL

## What I Did

- Inspected 100,000 employee records across 16 columns.
- Checked for missing values, duplicate records, and invalid performance scores.
- Cleaned text fields and converted columns to suitable data types.
- Changed performance scores outside the 1–5 range to missing values.
- Exported the cleaned data to a CSV file.
- Loaded the 100,000 records into the `dbo.Employees` table in SQL Server.
- Used SQL queries to check the data and calculate employee counts and salary statistics by department and country.

## Results

- 100,000 records loaded successfully.
- No exact duplicate rows or duplicate employee IDs were found.
- 100 invalid performance scores were changed to missing values.
- The final data contained 499 missing salaries, 599 missing performance scores, and 500 missing working-hours values.
- SQL validation found no performance scores outside the 1–5 range.

I kept missing values instead of filling them with assumed values.

## Files

- `inspect_data.py` — Checks the dataset and reports data quality issues.
- `clean_data.py` — Cleans the data and saves the CSV file.
- `load_to_sql.py` — Loads the cleaned CSV into SQL Server.
- `cleaning_report.txt` — Contains the cleaning summary.
- `pyproject.toml` — Lists the Python project dependencies.

## Running the Project

1. Download OpenML dataset ID 46557 and place the source file in the project folder as `dataset_`.
2. Install dependencies with `uv sync`.
3. Run `uv run python inspect_data.py`.
4. Run `uv run python clean_data.py`.
5. Create the `EmployeeDataEngineering` database and the `dbo.Employees` table in SQL Server.
6. Update the SQL Server connection settings in `load_to_sql.py` for your machine.
7. Run `uv run python load_to_sql.py`.
8. Use SQL Server Management Studio to run validation and analysis queries.

The source dataset and cleaned CSV are excluded from the Git repository.

## Possible Next Steps

- Add automated data quality tests.
- Use dbt to organize and test data transformations.
- Automate the pipeline.
