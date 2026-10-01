"""Fig 3: Kaplan-Meier curves by treatment arm."""
import pandas as pd
import matplotlib.pyplot as plt
from lifelines import KaplanMeierFitter

df = pd.read_csv("data/cohort_v2.csv")
for arm, color in [(0, "red"), (1, "green")]:
    KaplanMeierFitter().fit(df.time_days[df.treatment == arm], df.event[df.treatment == arm]).plot(color=color)
plt.savefig("fig3.pdf")
