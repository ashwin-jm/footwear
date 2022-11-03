import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

data = pd.read_csv('footwear.csv')

dict = {'Under Armour': [],
        'ASICS': [],
        'Nike': [],
        'Adidas': [],
        'PUMA': [],
        'Reebok': []}

for index, row in data.iterrows():
    brand = row.brand
    dict[brand].append(row.SalesPrice)

for ele in dict.keys():
    dict[ele] = [min(dict[ele]), max(dict[ele])]

entry_price = []
exit_price = []
for ele in dict.values():
    entry_price.append(ele[0])
    exit_price.append(ele[1])

brand = list(dict.keys())
x = np.arange(len(brand))
width = 0.45

fig, ax = plt.subplots()
rects1 = ax.bar(x - width/2, entry_price, width=width, label='Entry Price', color='steelblue')
rects2 = ax.bar(x + width/2, exit_price, width=width, label='Exit Price', color='tomato')

ax.set_ylabel('Price')
ax.set_title('Entry and Exit Price of each brand in running shoes category', fontsize=8.5)
ax.set_xlabel('Brand')
ax.set_xticks(x, brand)
ax.legend()

ax.bar_label(rects1, padding=2)
ax.bar_label(rects2, padding=2)

fig.tight_layout()

plt.show()