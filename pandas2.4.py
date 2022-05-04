import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('OnlineRetail.csv',encoding='ISO-8859-1')
# print(df.info())

# pivot1 = df.pivot_table(values='Quantity', index='InvoiceNo', columns='Country',aggfunc='mean')
# print(pivot1)

# pivot2 = df.pivot_table(values='Quantity', index='CustomerID', columns='StockCode',aggfunc={'max','min'})
# print(pivot2)

# pivot3 = df.pivot_table(values='UnitPrice', index='StockCode',aggfunc={'sum','mean'})
# print(pivot3)

# pivot4 = df.pivot_table(values='Quantity', index='StockCode',aggfunc='sum')
# print(pivot4)