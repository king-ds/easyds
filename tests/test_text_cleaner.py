import pandas as pd
from easyds.text_cleaner import feature_extraction

df = pd.DataFrame()
comments = ['This is good and easy to install', 'Ang bagal ng internet', 'Sana mas pabilisan pa ang serbisyo']
df['comments'] = comments
stop_words = ['ng', 'ikaw', 'and', 'is', 'pa', 'ang']


df = feature_extraction(df, 'comments', stop_words)

print(df)