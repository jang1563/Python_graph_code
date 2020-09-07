# Using test sample in seaborn

import seaborn as sns, matplotlib.pyplot as plt
sns.set(style="whitegrid")

tips = sns.load_dataset("tips")

sns.barplot(x="day", y="total_bill", data=tips, capsize=.1, ci="sd")
sns.swarmplot(x="day", y="total_bill", data=tips, color="0", alpha=.35)

plt.show()