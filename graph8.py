import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import statistics

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

mean_price = []
median_price = []
for ele in dict.keys():
    avg = statistics.mean(dict[ele])
    avg = round(avg,2)
    med = statistics.median(dict[ele])
    med = round(med,2)
    dict[ele] = [avg,med]
    mean_price.append(avg)
    median_price.append(med)


brand = list(dict.keys())
fig = plt.subplots(figsize =(12, 5))
br1 = np.arange(len(mean_price))
width = 0.45
br2 = [x+width for x in br1]

plt.bar(br1, mean_price, color="green", width=width, label="Mean Price")
plt.bar(br2, median_price, color="lime", width=width, label="Median Price")

plt.xlabel('Brand')
plt.ylabel('Price')
plt.title('Mean and Median Price of each Brand in running shoes category', fontsize=14)
plt.xticks([r+width for r in range(len(mean_price))], brand)
for index, value in enumerate(mean_price):
    y = value
    plt.text(index, y+2,
             str(value), ha='center')
for index, value in enumerate(median_price):
    y = value
    plt.text(index+width, y+2,
             str(value), ha='center')
plt.legend()

plt.show()