import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import os

os.chdir("/Users/ephraimlove/Courses/data_wrangling/")
df = pd.read_csv("data/R_lecture/daily-new-confirmed-covid-19-cases-per-million-people.csv", parse_dates=["Day"])

df.columns.values[2] = 'new_cases'

filtered = df[df["Entity"].isin(["United States", "Canada", "Brazil"])]
filtered = filtered[(filtered["Day"] >= "2021-01-01") & (filtered["Day"] <= "2021-03-01")]

summary = filtered.groupby(["Entity", "Day"])["new_cases"].sum().reset_index()

sns.lineplot(data=summary, x="Day", y="new_cases", hue="Entity")
plt.title("Daily New COVID-19 Cases")
plt.xticks(rotation=45)  # or 30, 60 depending on your preference
plt.tight_layout()       # optional: avoids label cutoff
plt.ylabel('New Cases')
plt.xlabel('')
plt.show()
