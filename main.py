# Pandas: Cannot setitem on a Categorical with a new category

import pandas as pd

df = pd.DataFrame({
    'A': [100, 0]
})

print(df)

df['A'] = pd.Categorical(df['A'])

df['A'] = df['A'].map({100: 'Yes', 0: 'No'})

print('-' * 50)

print(df)
