import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

data = pd.read_csv('footwear.csv')

dict = {'Under Armour': 0,
        'ASICS': 0,
        'Nike': 0,
        'Adidas': 0,
        'PUMA': 0,
        'Reebok': 0}

for index, row in data.iterrows():
    brand = row.brand
    if(row.Rating>=3.5):
            dict[brand]+=1

plt.figure(figsize=(10, 6))
plt.bar(list(dict.keys()), list(dict.values()), color='tomato')
plt.title('Average number of rating across each brand in running shoes category', fontsize=14)
plt.xlabel('Brand')
plt.ylabel('Number of Ratings')
for index, value in enumerate(list(dict.values())):
    plt.text(index, value+2,
             str(value))
plt.show()

