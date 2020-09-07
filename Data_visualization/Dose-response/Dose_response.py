#https://www.youtube.com/watch?v=uoshfzYW6vA

import pandas as pd

x = pd.read_excel('#FILENAME')
x.head()

t = x['time (min)'].values
y = x['y'].values


