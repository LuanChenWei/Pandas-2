import pandas as pd

#read file csv
df = pd.read_csv('FoodPrice_in_Turkey.csv')

# df1 = df.drop_duplicates(['ProductId'], keep= 'last')
# print(df1)

# df = df.drop_duplicates(['ProductId'], keep= 'last')
# print(df)

df_pro = df.loc[:,['ProductId','ProductName','UmId','UmName']]
# print(df_pro)

df_pri = df.loc[:,['ProductId','Place','Month','Year','Price']]
# print(df_pri)

# df_pri10 = df.loc[10:20,['ProductId','Place','Month','Year','Price']]
# df_pri10

# df1=pd.merge(df_pro,df_pri, on='ProductId')
# print(df1)

# df2=pd.concat([df_pro,df_pri], axis=1)
# print(df2)

df2=pd.concat([df_pro,df_pri,df_pri10], axis=1)
print(df2)
