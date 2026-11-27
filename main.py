# cd Pricing_Optimization
# python main.py
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

df = pd.read_csv("data/Sales.csv")
df = df.dropna()

# Found a repeated header as a value
df = df[df["Order ID"] != "Order ID"]

# cols to numeric value
df["Quantity Ordered"] = pd.to_numeric(df["Quantity Ordered"])
df["Price Each"] = pd.to_numeric(df["Price Each"])

# change date format
df["Order Date"] = pd.to_datetime(df["Order Date"],format="%m/%d/%y %H:%M")

# calc revenue
df["Revenue"] = (df["Quantity Ordered"] * df["Price Each"])

# Diplay products
print("\nProducts:")
# print(df["Product"].unique())

# saving cleaned data
# df.to_csv("data/cleaned.csv", index=False)


##############################
# EDA
##############################

#total quantity sold for each product
product_quantity = df.groupby("Product")[
    "Quantity Ordered"].sum().sort_values(ascending=False)
# print("\nQuantity Sold per Product:")
# print(product_quantity)

# total revenue for each product
product_revenue = df.groupby("Product")["Revenue"].sum().sort_values(ascending=False)
# print("\nRevenue by Product:")
# print(product_revenue)

#summary table
# aggregation >>>> more than one operation
summary = df.groupby("Product").agg(
    Total_Quantity=("Quantity Ordered", "sum"),
    Total_Revenue=("Revenue", "sum"))
# print(summary)
# summary.to_csv("data/Product_Summary.csv")


###################################################
# Plotting
###################################################

# plt.figure(figsize=(12, 6))
# product_revenue.sort_values().plot(kind="barh")
# plt.title("Total Revenue by Product")
# plt.xlabel("Total Revenue ($)")
# plt.ylabel("Product")
# plt.tight_layout()
# plt.savefig("data/revenues.png")
# plt.show()

# plt.figure(figsize=(12, 6))
# product_quantity.sort_values().plot(kind="barh")
# plt.title("Total Quantity Sold by Product")
# plt.xlabel("Quantity Sold")
# plt.ylabel("Product")
# plt.tight_layout()
# plt.savefig("data/quantities.png")
# plt.show()