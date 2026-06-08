"""
PwC Power BI Case Study - Retail Sales & Finance Analysis
Mumbai Electronics Conglomerate

Analyzes the provided star-schema data warehouse (Sales + Finance datasets)
to extract executive-level KPIs and insights.

Author: Aquib Azam Ansari
"""
import pandas as pd

# ============ SALES ANALYSIS ============
print("="*55)
print("SALES ANALYSIS")
print("="*55)

xl = pd.ExcelFile("Sales Dataset.xlsx")
salesfact   = pd.read_excel(xl, "salesfact")
dimproduct  = pd.read_excel(xl, "dimproduct")
dimpc       = pd.read_excel(xl, "dimprofitcenter")
dimshowroom = pd.read_excel(xl, "dimshowroom")
salestarget = pd.read_excel(xl, "salestarget")

# Join fact table with product dimension (star schema join)
sales = salesfact.merge(
    dimproduct[['id', 'category', 'brand']],
    left_on='skukey', right_on='id', how='left'
)

# KPI 1: Total Sales
print(f"\nTotal Gross Sales : Rs {salesfact['grosstotal'].sum():,.0f}")
print(f"Total Base Price  : Rs {salesfact['baseprice'].sum():,.0f}")
print(f"Transactions      : {len(salesfact)}")
print(f"Units Sold        : {salesfact['qty'].sum()}")

# KPI 2: Sales by Category
print("\nSales by Category:")
print(sales.groupby('category')['grosstotal'].sum().sort_values(ascending=False).to_string())

# KPI 3: Sales by Brand
print("\nSales by Brand:")
print(sales.groupby('brand')['grosstotal'].sum().sort_values(ascending=False).to_string())

# KPI 4: Sales by Transaction Type
print("\nSales by Type:")
print(salesfact.groupby('salestype')['grosstotal'].sum().sort_values(ascending=False).to_string())

# KPI 5: Target vs Actual
print(f"\nTotal Sales Target: Rs {salestarget['targetamount'].sum():,.0f}")
achievement = salesfact['grosstotal'].sum() / salestarget['targetamount'].sum() * 100
print(f"Achievement %     : {achievement:.1f}%")

# ============ FINANCE ANALYSIS ============
print("\n" + "="*55)
print("FINANCE ANALYSIS")
print("="*55)

xlf = pd.ExcelFile("Finance Dataset.xlsx")
financefact = pd.read_excel(xlf, "financefact")
glmapping   = pd.read_excel(xlf, "generalledgermapping")
targetfact  = pd.read_excel(xlf, "targetfact")
budgetfact  = pd.read_excel(xlf, "budgetfact")

# Join finance fact with GL mapping (to categorize amounts)
finance = financefact.merge(
    glmapping[['id', 'category1', 'category2']],
    left_on='glmappingkey', right_on='id', how='left'
)

print(f"\nTotal Finance Postings : Rs {financefact['amount'].sum():,.2f}")
print(f"Target Revenue (total) : Rs {targetfact['revenueamt'].sum():,.0f}")

print("\nAmounts by GL category:")
print(finance.groupby('category1')['amount'].sum().sort_values(ascending=False).to_string())

print("\nDone. These KPIs feed the Power BI CXO dashboards.")
