import pandas as pd
from .debt_dynamics import project_debt_path

def run_scenarios(baseline, shock_scenarios, years):
    """
    Takes a baseline path and shock inputs and returns a combined dataframe
    """
    outputs = []
    for _, row in shock_scenarios.iterrows():
        growth = row["Growth_Shock"] / 100
        rate = row["Interest_Shock"] / 100
        primary = row["Primary_Shock"] / 100

        df = project_debt_path(
            baseline=baseline,
            growth=growth,
            rate=rate,
            primary=primary,
            years=years
        )
        df["Scenario"] = row["Scenario"]
        outputs.append(df)

    return pd.concat(outputs, ignore_index=True)
