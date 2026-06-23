import pandas as pd

# Load raw CUNY expenditure data
# Make sure this CSV file is in the same folder as this Python script.
df = pd.read_csv("CUNY_Community_College_Expenditures_By_Source.csv")

# Clean column names so they are easier to use in Python/SQL-style analysis
df.columns = (
    df.columns
    .str.strip()
    .str.lower()
    .str.replace(" ", "_", regex=False)
    .str.replace("/", "_", regex=False)
)

# Keep only the useful columns for the dashboard
# Expected columns after cleaning:
# fiscal_year, actual_forecast, source, amount
df = df[["fiscal_year", "actual_forecast", "source", "amount"]]

# Use only actual historical data, not forecast data
df = df[df["actual_forecast"].str.upper() == "ACTUAL"]

# Make sure Amount is numeric
df["amount"] = pd.to_numeric(df["amount"], errors="coerce")

# Remove blank rows and duplicate rows
df = df.dropna()
df = df.drop_duplicates()

# Save the cleaned dataset
output_file = "cuny_expenditures_actual.csv"
df.to_csv(output_file, index=False)

print(f"Cleaned data saved successfully as {output_file}")
print(df.head())
