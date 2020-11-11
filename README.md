# easyds

Personal Python library to make usual data science workflow easy.


Sample usage
```
import pandas as pd
from easyds.data_cleaner import basic_clean

df = pd.DataFrame()

str_numbers = ['1', '2', '3']
df['str_Numbers'] = str_numbers

str_date = ['1998/10/29', '1998/10/30', '1998/10/31']
df['STR DaTe'] = str_date

str_float = ['1.0', '1.3', '4.4  ']
df['Str Float'] = str_float

numbers = [1, '2', '3']
df['NuMbeRs'] = numbers

clean_df = basic_clean(df)
```
