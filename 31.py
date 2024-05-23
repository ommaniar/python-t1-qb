# Consider the following autompg dataset:
# https://raw.githubusercontent.com/Jovita7/Data-Analysis-and-Visualization/main/auto-mpg.csv
# Write Python code to convert it to a DataFrame and remove mpg and cylinders columns from it
import pandas as pd
df = pd.read_csv("csv_files/auto-mpg.csv")
print(df.drop(columns=["mpg",'cylinders']))
