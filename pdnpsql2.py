import pandas as pd
import numpy as np
a='bios.csv'
c=pd.read_csv(a)
print(c)
print(c.head(5))
print(c.columns)
print(c.dtypes)
print(c.isna())
print(c[c['height_cm']>160][['height_cm','name']])#instead of asalsry im doing these
print(c.loc[0:4,'height_cm'])
print(c['born_country'].isin(['japan']))
print(c[['name','height_cm']])
print(c['height_cm'].interpolate())
#print(c['height_cm'].isna().sum())
#c['height_cm']=c['height_cm'].interpolate()
print(c['height_cm'])
print(c.groupby('born_country')['height_cm'].mean())
print(c.groupby('born_country').agg({'height_cm':'sum','weight_kg':'mean'}))
print(c.groupby('born_country')['height_cm'].agg(['mean','sum']))
print(c.groupby('born_country')['athlete_id'].value_counts().sum())
print(c.groupby('born_country').agg({'athlete_id':'sum'}))
print(c.groupby('born_country')['athlete_id'].agg(['sum']))
c['borndates']=pd.to_datetime(c['born_date'])
print(c['borndates'].dt.year)
c['height_cat']=c['height_cm'].apply(lambda x:'low'if x < 160 else 'medium' if x > 175 else 'tall' )
print(c['height_cat'])
#print(c['borndates'].dt.year.value_counts())
c['year']=c['borndates'].dt.year
print(c.groupby('year')['athlete_id'].value_counts())#values count gives yiu the largest number 
#print(c['born_country'].count())
#print(c.groupby('year')['athlete_id'].value_counts().sum())
#print(c.sort_values(by='height_cm',ascending=False)['height_cm'])
#print(c.groupby('year')['athlete_id'].count())# used count when groupby to tell the athleted id on that groupby 
#print(c['born_country'].value_counts())
#print(c.groupby('born_country')['athlete_id'].count())
print(c.groupby('born_country')['athlete_id'].value_counts())
print(c['born_country'].value_counts())
