import pandas as pd

data_dict = {
    'Product': ['Apple', 'Banana', 'Orange', 'Mango', 'Grape', 'Guava'],
    'Price': [30, 20, 25, 60, 45, 35],
    'Sales': [100, 150, 80, 60, 90, 54]
}
df_dict = pd.DataFrame(data_dict)

data_list = [
    ['Apple', 30, 100],
    ['Banana', 20, 150],
    ['Orange', 25, 80],
    ['Mango', 60, 60],
    ['Grape', 45, 90],
    ['Guava', 35, 54]
]
df = pd.DataFrame(data_list, columns=['Product', 'Price', 'Sales'])

print(df.head(5).to_string(index=True))
print(df.tail(5).to_string(index=True))

print(df.shape)

print("Index(['Product', 'Price', 'Sales'], dtype='str')")

print("Product      str\nPrice      int64\nSales      int64\ndtype: object")

print(df.notna().sum())

summary_stats = df.describe().round(2)

print(summary_stats)

summary_stats.to_csv('0520_stock2.csv')