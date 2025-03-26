import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import os

# Sample data (you'd replace this with your actual DataFrame)
os.chdir("/Users/ephraimlove/Courses/data_wrangling/")
df = pd.read_csv("data/R_lecture/daily-new-confirmed-covid-19-cases-per-million-people.csv", parse_dates=["Day"])

df.columns.values[2] = 'new_cases'

# Filter and subset the countries
countries = ["United States", "Canada", "Brazil"]
df = df[df["Entity"].isin(countries)]

# Convert to ordered category (like factor levels in R)
df["Entity"] = pd.Categorical(df["Entity"], categories=countries, ordered=True)

# Optional: aggregate data (if needed)
df_summary = (
    df.groupby(["Entity", "Day"])["new_cases"]
    .sum()
    .reset_index()
)

# Set Seaborn theme
sns.set_theme(style="whitegrid")

# Create the FacetGrid
g = sns.FacetGrid(
    df_summary,
    col="Entity",
    col_order=countries,
    col_wrap=1,                # one column layout (like facet_wrap with ncol = 1)
    height=3.5,
    aspect=2,
    sharey=False
)

# Plot each facet
g.map_dataframe(sns.lineplot, x="Day", y="new_cases", color="steelblue")

# Rotate x-axis labels
for ax in g.axes.flatten():
    ax.tick_params(axis='x', rotation=45)

# Add a title and labels
g.set_titles("{col_name}")
g.set_axis_labels("", "New Cases")
g.fig.subplots_adjust(top=0.9)
g.fig.suptitle("Daily New COVID-19 Cases by Entity", fontsize=16)

plt.tight_layout()
plt.show()
