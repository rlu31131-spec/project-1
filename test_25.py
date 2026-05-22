import pandas as pd

df = pd.read_csv('Grocery_Inventory_and_Sales_Dataset.csv')

df['Unit_Price_Clean'] = df['Unit_Price'].str.replace('$', '', regex=False).str.strip().astype(float)


print("=" * 60)
print(" (1) 每個商品的總庫存價值")
print("=" * 60)

df['Total_Inventory_Value'] = df['Unit_Price_Clean'] * df['Stock_Quantity']

print(df[['Product_ID', 'Product_Name', 'Stock_Quantity', 'Unit_Price', 'Total_Inventory_Value']].head(10).to_string(index=False))
print(f"\n💡 全店所有商品的【總庫存資產價值】累計為: ${df['Total_Inventory_Value'].sum():,.2f}")
print("\n" + "-" * 60 + "\n")


print("=" * 60)
print(" 🥇 (2) 找出最暢銷的商品")
print("=" * 60)

max_sales = df['Sales_Volume'].max()
top_sellers = df[df['Sales_Volume'] == max_sales]

print(f"經分析，您資料集裡最高銷售量為 {max_sales} 件，並列冠軍的商品名單如下：")
print(top_sellers[['Product_ID', 'Product_Name', 'Catagory', 'Sales_Volume']].to_string(index=False))
print("\n" + "-" * 60 + "\n")


print("=" * 60)
print(" 💰 (3) 計算 9 折後的收入")
print("=" * 60)

df['Original_Revenue'] = df['Unit_Price_Clean'] * df['Sales_Volume']

df['Discounted_Revenue_90'] = df['Original_Revenue'] * 0.9

print(f"🛒 所有商品在打 9 折促銷後的【總收入】為: ${df['Discounted_Revenue_90'].sum():,.2f}")
print("=" * 60)