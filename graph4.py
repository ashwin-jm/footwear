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
    dict[brand].append(row.Discount)

brand = []
avg_values = []
for ele in dict.keys():
    avg = sum(dict[ele])/len(dict[ele])
    dict[ele] = round(avg,2)
    brand.append(ele)
    avg_values.append(dict[ele])

df = pd.DataFrame(dict, index=[0])
df.to_csv('graph4.csv')

plt.figure(figsize=(12, 5))
plt.barh(brand, avg_values, color='limegreen')
plt.title('Average discount percentage across each brand in running shoes category', fontsize=14)
plt.xlabel('Average Discount Percentage')
plt.ylabel('Brand')
for index, value in enumerate(avg_values):
    plt.text(value, index,
             str(value))

plt.show()

