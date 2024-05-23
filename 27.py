# Create a Pandas DataFrame from the following table and write code to remove all rows from this table only if all of their values are NaN
import pandas as pd
import numpy as np
d = {
    "name":["Willam","Emma","Sofia","Markus","Edward","Thomas","Ethan",np.nan,"Arun","Anika","Paulo"],
    "region": [np.nan,"North","East",np.nan,"West","West","South",np.nan,"West","East","South"],
    "sales": [50000,52000,None,None,42000,72000,49000,None,67000,65000,670000],
    "Expenses":[42000,43000,None,None,38000,39000,420000,None,3900,50,56]
}

df = pd.DataFrame(d)
print(df.dropna(how="all"))
