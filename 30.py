# Convert this to a Pandas DataFrame and remove duplicate rows from it. Reset index values.
data = {
    "A": ["TeamA", "TeamB", "TeamB", "TeamC", "TeamA"],
    "B": [50, 40, 40, 30, 50],
    "C": [True, False, False, False, True]
}

import pandas as pd
data = pd.DataFrame(data)
print(data.drop_duplicates(ignore_index=True))
