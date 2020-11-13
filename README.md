# easyds

Personal Python library to make usual data science workflow easy.

I created this package to lessen my time when doing ds task. 
All of the features that I've established were tested in real world problems. 
Feel free to contribute and suggest for further improvement.

# Installation
```python
pip install easyds
```

# Sample usage

### basic_clean

Gives an usual cleaning to your data.
```
import pandas as pd
from easyds.data_cleaner import basic_clean

# create sample data
df = pd.DataFrame()

str_numbers = ['1', '2', '3']
df['str_Numbers'] = str_numbers

str_date = ['1998/10/29', '1998/10/30', '1998/10/31']
df['STR DaTe'] = str_date

str_float = ['1.0', '1.3', '4.4  ']
df['Str Float'] = str_float

numbers = [1, '2', '3']
df['NuMbeRs'] = numbers
```

| str_Numbers   | STR DaTe   |Str Float  | NuMbeRs|
|---------------|:----------:|:---------:|-------:|
|1              | 1998/10/29 |1.0        |1       |     
|2              | 1998/10/30 |1.3        |2       |
|3              | 1998/10/31 |4.4        |3       |
```
df.dtypes
str_Numbers       object
STR DaTe          object
Str Float         object
NuMbeRs           object
```

After <i>basic_clean</i>,
| str_numbers   | str_date   |str_float|numbers|
|---------------|:----------:|:-------:|------:|
|1              | 1998/10/29 |1.0      |1      |     
|2              | 1998/10/30 |1.3      |2      |
|3              | 1998/10/31 |4.4      |3      |
```
df.dtypes
str_Numbers       int64
STR DaTe          datetime64[ns]
Str Float         float64
NuMbeRs           int64
```


### feature_extraction

Clean the corpus input into its most useful form.
This is helpful for those interested in text analysis.

Sample usage

```
import pandas as pd
from easyds.text_cleaner import feature_extraction

# create sample data
df = pd.DataFrame()
comments = ['This is good and easy to install', 'Ang bagal ng internet', 'Sana mas pabilisan pa ang serbisyo']
df['comments'] = comments

# i define my own collection of stop words
stop_words = ['ng', 'ikaw', 'and', 'is', 'pa', 'ang']
```
|comments                          |
|----------------------------------|
|This is good and easy to install  |   
|Ang bagal ng internet             |
|Sana mas pabilisin pa ang serbisyo|

After <i>feature_extraction</i>,
```
df = feature_extraction(df, 'comments', stop_words)
```
|comments                          |new_comments                    |
|----------------------------------|-------------------------------:|
|This is good and easy to install  |[this, good, easy, install]     |
|Ang bagal ng internet             |[bagal, internet]               |
|Sana mas pabilisin pa ang serbisyo|[sana, mas, pabilisin, serbisyo]|

