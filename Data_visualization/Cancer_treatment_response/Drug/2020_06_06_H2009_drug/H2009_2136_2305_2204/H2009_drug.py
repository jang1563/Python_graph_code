import numpy as np
import pandas as pd



import matplotlib.pyplot as plt
import seaborn as sns

%matplotlib inline

data = pd.read_excel('H2009_drug.xlsx')

data.head()

df = data.pivot('Conc. (uM)', 'Drug', 'A540')

df.head()

sns.heatmap(df, annot=True, fmt='.2f')
plt.title('Heatmap of H2009 cell', fontsize=20)
plt.savefig('H2009 hetamap annotation')


