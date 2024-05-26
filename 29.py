# Write Python code to remove outliers from any given DataFrame.
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

df = pd.read_csv("csv_files/titanic.csv")

print(df["fare"])
def remove_outliers(df,col):
    Q1 = df[col].quantile(0.25)
    Q3 = df[col].quantile(0.75)
    IQR = Q3 - Q1
    min = Q1 -1.5 * IQR
    max = Q3  + 1.5 * IQR
    df[(df[col]>= max) & (df[col] <= min)] = df[col].mean
    return df
df = remove_outliers(df,"fare")

print(df["fare"])
df.boxplot()
plt.show()