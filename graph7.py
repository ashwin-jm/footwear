import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

data = pd.read_csv('footwear.csv')

dict = {'1-10': 0,
        '10-20': 0,
        '20-30': 0,
        '30-40': 0,
        '40-50': 0,
        '50-60': 0,
        '60-70': 0}

d = []
for index, row in data.iterrows():
    discount = row.Discount
    if(discount>=1 and discount<10):
        dict['1-10']+=1
    elif(discount>=10 and discount<20):
        dict['10-20']+=1
    elif(discount>=20 and discount<30):
        dict['20-30']+=1
    elif (discount >= 30 and discount < 40):
        dict['30-40']+=1
    elif (discount >= 40 and discount < 50):
        dict['40-50']+=1
    elif (discount >= 50 and discount < 60):
        dict['50-60']+=1
    elif (discount >= 60 and discount < 70):
        dict['60-70']+=1

discount_range = []
count = []
for ele in dict.keys():
    discount_range.append(ele)
    count.append(dict[ele])



plt.figure(figsize=(10, 6))
plt.bar(discount_range, count, color='mediumturquoise')
plt.title('Discount range across all products in running shoes category', fontsize=14)
plt.xlabel('Discount Range')
plt.ylabel('Number of products')
for index, value in enumerate(count):
    plt.text(index, value+1,
             str(value))
plt.show()

