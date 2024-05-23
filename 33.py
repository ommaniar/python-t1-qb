# Use the file ipl-matches.csv which contains data of all the IPL matches from year 2008 to 2022. Read this csv file and display the basic
# information like memory and data types for this data frame. Write python code for the following cases:
# 1. List out all matches gone in superover.
# 2. How Many Matches won by Chennai Super Kings at Kolkata.
# 3. In How Many Matches MS Dhoni is Player of Match Vs Mumbai Indians.
# 4. Display list of all matches in which Gujarat Titans won the Toss and Elected to Bat and won the match.
# 5. Display list of all matches won by Gujarat Titans.
import pandas as pd
df = pd.read_csv("csv_files/ipl-matches.csv")
print(df.keys())
print(df[df["SuperOver"]!="N"].style)