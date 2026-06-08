# PwC Case Study 1 — Problem Breakdown & Learnings

## The Query (What was asked)

A Mumbai electronics retail conglomerate needed to move from gut-feel to data-driven decisions.
The deliverable: two executive (CXO) Power BI dashboards — Sales and Finance — built from a
provided data-warehouse dataset, designed for fast executive decision-making.

## The Solution Approach

1. **Understand the architecture:** Data flows from source (AWS Redshift / Excel) → Power Query
   (clean & transform) → DAX (calculate KPIs) → Dashboards → Power BI Service (publish/share).
2. **Model the data:** Connect the fact tables (salesfact, financefact) to dimension tables
   (date, product, location) using keys — this is a star schema.
3. **Build KPIs in DAX:** Sales Amount, YTD Sales, Achievement % for sales; Revenue, COGS,
   Gross Profit, EBITDA, Net Profit for finance.
4. **Design two CXO dashboards:** clean, interactive, executive-friendly.

## What I Learned (transferable skills)

**1. Star schema is the foundation of business intelligence.**
Real business data is never one flat table. It is split into FACT tables (what happened —
transactions, targets) and DIMENSION tables (context — who, what, where, when). Learning to
identify and join them is the single most important BI skill.

**2. KPIs come from the business question, not the data.**
Executives don't want rows — they want answers: "Are we hitting target? What's our profit?
Which product wins?" The analyst's job is to translate business questions into DAX measures.

**3. Actual vs Target (Achievement %) is the heartbeat of executive reporting.**
Achievement % = (Actual / Target) × 100. This single KPI appears in almost every corporate
dashboard and is the fastest way to show performance against goals.

**4. Sales and Finance are two lenses on one business.**
Sales measures revenue and volume. Finance measures profitability:
Revenue − COGS = Gross Profit, then − OPEX − Tax = Net Profit. Executives need both views.

**5. The CXO dashboard mindset = simplicity.**
One screen, big numbers, clear trends, minimal clutter. The goal is a 30-second read, not a
display of every chart type available.

## How This Helps Me Solve Similar Problems

Any future BI task now follows the same playbook: find the fact and dimension tables, model the
relationships, translate the stakeholder's questions into KPIs, and design a clean dashboard that
answers those questions at a glance. This pattern repeats across retail, finance, healthcare, and
agriculture — the domain changes, but the method stays the same.
