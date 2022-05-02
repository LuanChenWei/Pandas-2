import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('GDPlist.csv',encoding='ISO-8859-1')
# df.info()

# df_GDP = df.loc[:,'GDP']
# df_GDP.max()
# df_GDP.min()

# df_GDP.mode()
# df_GDP.median()
# df_GDP.mean()

# a= plt.hist(df.GDP, bins=200)
# print(a)

# df_conti = df['Continent'].mode()
# print(df_conti)

# df_sum = df.groupby('Continent')['GDP'].sum()
# df_mean = df.groupby('Continent')['GDP'].mean()
# # print(df_sum,df_mean)
# df_merge = pd.merge(df_sum,df_mean, on='Continent')
# print(df_merge)
# df_merge.rename(columns={'GDP_x':'Tong GDP','GDP_y':'TBC GDP'},inplace=True)