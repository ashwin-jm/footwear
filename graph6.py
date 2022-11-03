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
    dict[brand].append(row.Rating)

brand = []
avg_rating = []
for ele in dict.keys():
    avg = sum(dict[ele])/len(dict[ele])
    dict[ele] = round(avg,2)
    brand.append(ele)
    avg_rating.append(dict[ele])


df = pd.DataFrame(dict, index=[0])
df.to_csv('graph6.csv')
plt.figure(figsize=(10, 6))
plt.bar(brand, avg_rating, color='orange')
plt.title('Average rating across each brand in running shoes category', fontsize=14)
plt.xlabel('Brand')
plt.ylabel('Average Rating')
for index, value in enumerate(avg_rating):
    plt.text(index, value+0.05,
             str(value))
plt.show()