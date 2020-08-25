# Using test sample in seaborn

import seaborn as sns, matplotlib.pyplot as plt
import numpy as np
import pandas as pd

%matplotlib inline

sns.set(style="whitegrid")

data = pd.read_excel('2136_bar_graph.xlsx')

sns.barplot(x="Conc. (uM)", y="normalized A540", data=data, capsize=.3, ci="sd")
sns.swarmplot(x="Conc. (uM)", y="normalized A540", data=data, color="0", alpha=.35)

plt.show()
sns.barplot(x="Conc. (uM)", y="normalized A540", data=data, capsize=.3, ci="sd")
sns.swarmplot(x="Conc. (uM)", y="normalized A540", data=data, color="0", alpha=.35)

plt.title('H2009 with 2136', fontsize=20)
plt.savefig('H2009_2136', dpi = 300)