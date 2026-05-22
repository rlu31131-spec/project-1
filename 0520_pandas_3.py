import pandas as pd

file_name = 'SuperMarket Analysis.csv'
df = pd.read_csv(file_name)

print("=== 1. 資料筆數與前 5 筆內容 ===")
print(f"總資料筆數: {len(df)} 筆")
print(df.head())
print("-" * 50)


filtered_df = df[(df['Branch'] == 'A') & (df['Customer type'] == 'Member')]
print("=== 2. 篩選 Branch 為 A 且 Customer type 為 Member ===")
print(f"篩選後的交易筆數: {len(filtered_df)} 筆")
print(filtered_df.head())
print("-" * 50)

product_summary = df.groupby('Product line').agg(
    Total_Sales=('Sales', 'sum'),
    Average_Rating=('Rating', 'mean')
).round(2)

print("=== 3. 各產品線的總銷售額與平均評分 ===")
print(product_summary)
print("-" * 50)


city_gender_summary = df.groupby(['City', 'Gender']).agg(
    Average_Sales=('Sales', 'mean'),
    Transaction_Count=('Invoice ID', 'count')
).round(2)

print("=== 4. 依 City 與 Gender 分組的平均銷售額與交易筆數 ===")
print(city_gender_summary)
print("-" * 50)


top_product = product_summary['Total_Sales'].idxmax()
top_sales_value = product_summary['Total_Sales'].max()
print("=== 5. 總銷售額最高的產品線 ===")
print(f"最高總銷售額產品線: {top_product} (總銷售額: {top_sales_value})")
print("-" * 50)


output_file = '0520_pandas_3OK.CSV'
product_summary.to_csv(output_file, encoding='utf-8-sig')
print(f"=== 6. 檔案匯出成功！已儲存至 {output_file} ===")