import pandas as pd
from pandas.io.parsers import read_csv

df=pd.read_csv("cities.csv", index_col=False)
df.set_index('City_ID', inplace=True)
print(df.head())
html=df.to_html()
print(html)
text_file = open("data.html", "w")
text_file.write(html)
text_file.close()