# DAX Measures — PwC Case Study (Sales + Finance KPIs)

These are the core DAX measures from the case study, used to build the CXO dashboards.

## Sales KPIs

```dax
-- Total Sales Amount
Sales Amount = SUM('SalesFact'[basePrice])

-- Total Sales Quantity
Sales Quantity = SUM('SalesFact'[Qty])

-- Year-to-Date Sales Amount
YTD Sales Amount =
VAR selected_start_date = DATE(YEAR(MAX(dimDate[FullDateAlternateKey])), 1, 1)
VAR selected_end_date   = MAX(dimDate[FullDateAlternateKey])
RETURN
CALCULATE(
    SUM('SalesFact'[basePrice]),
    dimDate[FullDateAlternateKey] >= selected_start_date &&
    dimDate[FullDateAlternateKey] <= selected_end_date
)

-- Achievement % (Quantity): Actual vs Target
Achievement Qty % = IFERROR([YTD_sales_qty] / [YTD_Budget_Qty], 0)

-- Achievement % (Amount): Actual vs Target
Achievement Amount % = IFERROR([YTD_sales_Amt] / [YTD_Budget_Amt], 0)
```

## Finance KPIs

```dax
-- Revenue (Net Sales)
Total Revenue = ABS(
    CALCULATE(SUM('FinanceFact'[Amount]), 'AccountDimension'[category1] = "Net Sales")
)

-- COGS (Cost of Goods Sold)
COGS = CALCULATE(SUM('FinanceFact'[Amount]), 'AccountDimension'[category1] = "COGS Total")

-- Gross Profit
Gross Profit = [Total Revenue] - [COGS]

-- EBITDA
EBITDA = [Gross Profit] + [Other Income] - [Total Operating Expense]
         + ABS([Dep RoU Asset]) + ABS([Dep Amort]) + ABS([Factory Depreciation])
         + [Lease Finance Interest]

-- Net Profit After Tax
Net Profit = [Profit before taxes] - [Deferred tax] - [Income tax expense]

-- OPEX (Operating Expenses)
Total Operating Expense = [Total Administrative Expenses] + [Total Selling & Distribution Expenses]
```

## Key Concepts

- **CALCULATE** — changes the filter context of a measure (the most important DAX function).
- **VAR** — stores a value for reuse and readability within a measure.
- **IFERROR** — prevents divide-by-zero errors in ratio KPIs like Achievement %.
- **ABS** — used on finance amounts since some GL postings are stored as negatives.
