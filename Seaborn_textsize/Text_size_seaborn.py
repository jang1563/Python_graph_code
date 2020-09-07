import seaborn as sns
import matplotlib.pyplot as plt
from numpy import arange
# here set the scale by 3
sns.set(font_scale=3)
x = arange(25).reshape(5, 5)
cmap = sns.diverging_palette(220, 20, sep=20, as_cmap=True)
ax = sns.heatmap(x, cmap=cmap)
plt.show()
