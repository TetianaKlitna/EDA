# Filter the DataFrame for object columns
non_numeric = planes.select_dtypes("object")

print(non_numeric)

# Loop through columns
for col in non_numeric.columns:
  # Print the number of unique values
  print(f"Number of unique values in {col} column: ", non_numeric[col].nunique())