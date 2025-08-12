import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
df = pd.read_csv(r"C:\MINI PROJECT\PRODIGY\TASK1\TASK1.csv")
print(df.head(), "\nColumns:", df.columns.tolist())
def plot_bar(col, title, filename, palette):
    plt.figure(figsize=(10,6))
    sns.countplot(x=col, data=df, palette=palette)
    plt.title(title)
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.savefig(filename, dpi=300)
    plt.show()
plot_bar('Region', "Countries per Region", "region_distribution.png", 'viridis')
plot_bar('IncomeGroup', "Countries per Income Group", "income_group_distribution.png", 'coolwarm')
