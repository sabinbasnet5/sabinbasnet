import pandas as pd

# Example DataFrame with missing values
data = {
    'A': [1, 2, None, 4],
    'B': [None, 2, 3, 4],
    'C': [1, None, None, 4]
}
df = pd.DataFrame(data)

# Using dropna
df_cleaned = df.dropna()

print (df_cleaned)