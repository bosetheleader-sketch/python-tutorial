import pandas as pd

# Create Dataset
employees = {
    "Employee_ID": [101, 102, 103, 104, 105],
    "Name": ["John", "Alice", "Bob", "Emma", "David"],
    "Department": ["IT", "HR", "IT", "Finance", "HR"],
    "Age": [25, 30, 28, 35, 26],
    "Salary": [60000, 50000, 70000, 80000, 55000],
    "Experience": [2, 5, 4, 8, 3]
}

df = pd.DataFrame(employees)

print("\nEmployee Dataset")
print(df)

# -----------------------------
# Basic Information
# -----------------------------

print("\nDataset Info")
print(df.info())

print("\nSummary Statistics")
print(df.describe())

# -----------------------------
# Filtering
# -----------------------------

print("\nEmployees with Salary > 60000")
print(df[df["Salary"] > 60000])

# -----------------------------
# Sorting
# -----------------------------

print("\nSorted by Salary (Highest First)")
print(df.sort_values(by="Salary", ascending=False))

# -----------------------------
# Group By
# -----------------------------

print("\nAverage Salary by Department")
print(df.groupby("Department")["Salary"].mean())

# -----------------------------
# Add New Column
# -----------------------------

df["Bonus"] = df["Salary"] * 0.10

print("\nDataset with Bonus")
print(df)

# -----------------------------
# Highest Paid Employee
# -----------------------------

highest = df.loc[df["Salary"].idxmax()]

print("\nHighest Paid Employee")
print(highest)

# -----------------------------
# Update Salary
# -----------------------------

df.loc[df["Department"] == "IT", "Salary"] += 5000

print("\nUpdated IT Salaries")
print(df)

# -----------------------------
# Save to CSV
# -----------------------------

df.to_csv("employees.csv", index=False)

print("\nData saved to employees.csv")
