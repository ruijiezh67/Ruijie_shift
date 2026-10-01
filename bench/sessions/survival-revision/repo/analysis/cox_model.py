"""Main cause-specific Cox model (run on lab-ws2)."""
import pandas as pd
from lifelines import CoxPHFitter

df = pd.read_csv("data/cohort_v2.csv")
cph = CoxPHFitter()
cph.fit(df[["time_days", "event", "age", "treatment"]].dropna(), "time_days", "event")
cph.print_summary()
