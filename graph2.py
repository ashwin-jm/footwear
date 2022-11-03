import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

data = pd.read_csv('footwear.csv')
dict = {}
for index, row in data.iterrows():
    brand = row.brand
    if brand in dict.keys():
        discount = row.Discount
        if(discount==0):
            dict[brand][0]+=1
        else:
            dict[brand][1]+=1
    else:
        discount = row.Discount
        if(discount==0):
            dict[brand] = [1,0]
        else:
            dict[brand] = [0,1]

brand = list(dict.keys())
without_discount = []
with_discount = []
for ele in dict.values():
    without_discount.append(ele[0])
    with_discount.append(ele[1])
x = np.arange(len(brand))
width = 0.40

fig, ax = plt.subplots()
rects1 = ax.bar(x - width/2, with_discount, width, label='With discount', color='skyblue')
rects2 = ax.bar(x + width/2, without_discount, width, label='Without discount', color='dodgerblue')

ax.set_ylabel('Number of products')
ax.set_title('Number of Products with and without Discount each brand have in the running shoes category', fontsize=8.5)
ax.set_xlabel('Brand')
ax.set_xticks(x, brand)
ax.legend()

ax.bar_label(rects1, padding=2,)
ax.bar_label(rects2, padding=2)

fig.tight_layout()

plt.show()