import matplotlib.pyplot as plt

brand = ['Adidas', 'ASICS', 'Nike', 'PUMA', 'Reebok', 'Under Armour']
no_of_products = [195, 134, 170, 53, 30, 50]

plt.figure(figsize=(7, 5))
plt.bar(brand, no_of_products, width=0.5)
plt.title('No of products of each brand in running shoes category')
plt.xlabel('Brand')
plt.ylabel('Number of products')
for index, value in enumerate(no_of_products):
    plt.text(index, value+2,
             str(value), ha='center')
plt.show()