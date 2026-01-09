import pandas as pd

def project_debt_path(baseline, growth, rate, primary, years):
    """
    Core debt dynamics:
        d(t+1) = ((1+r)/(1+g)) * d(t) - pb(t)
    where all terms are in % of GDP
    """
    out = baseline.copy()
    start_year = int(out["Year"].max()) + 1
    debt_gdp = out["Debt_GDP"].iloc[-1]

    rows = []
    for i in range(years):
        year = start_year + i
        debt_gdp = ((1 + rate) / (1 + growth)) * debt_gdp - primary
        interest_gdp = debt_gdp * rate
        required_primary = ((1 + rate) / (1 + growth)) * debt_gdp - debt_gdp

        rows.append({
            "Year": year,
            "Debt_GDP": debt_gdp,
            "Interest_GDP": interest_gdp,
            "Required_Primary": required_primary,
            "Growth": growth,
            "Rate": rate,
            "Primary_Balance": primary
        })

    return pd.concat([out, pd.DataFrame(rows)], ignore_index=True)
