# Use the file heights_weights.csv (https://raw.githubusercontent.com/Jovita7/Data-Analysis-and-Visualization/main/heights_weights.csv)
# which contains 10000 non-null values for heights and weights. The Male column shows 1 if the person is a Male and 0 if the person is a Female.
# 1. Convert this file into a pandas Data Frame. (0.5 marks)
# 2. Display basic information like memory and data types for this data frame. (0.5 marks)
# 3. Display basic statistics like mean, std, quartiles, etc. for this data frame. (0.5 marks)
# 4. Create a correlation table for the data frame and comment about what kind of correlation is there between Height and Weight. (0.5
# marks)
# 5. Do Height and Weight contain any outliers? (1 mark)

import pandas as pd
data = pd.read_csv("csv_files/heights_weights.csv")
# 2
print(data.info(memory_usage=True))
# 3
print(data.describe())
print("correlation")
# 4
print(data.corr(numeric_only=True))
print(data.corr(numeric_only=True)["Height"]["Weight"])
# 5
def outliers(data,column):
    Q1 = data[column].quantile(0.25)
    Q3 = data[column].quantile(0.75)
    IQR = Q3 - Q1
    return data[(data[column] < Q1 - 1.5 * IQR) | (data[column] > Q3 + 1.5 * IQR)]


for i in ["Weight","Height"]:
    print(i)
    print(outliers(data,i))