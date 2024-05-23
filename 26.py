# Create a Pandas DataFrame from the following table and write code to remove all rows from this table containing at least one NaN value
import pandas as pd
df = pd.read_csv("csv_files/titanic.csv")
print(df.dropna())

