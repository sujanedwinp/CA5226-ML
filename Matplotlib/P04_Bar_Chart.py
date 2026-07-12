import matplotlib.pyplot as plt

products = ["Laptop", "Phone", "Tablet", "Watch", "Headphones"]
sales    = [120, 350, 95, 210, 180]

plt.bar(products, sales, color=["steelblue", "tomato", "seagreen", "gold", "mediumpurple"])
plt.title("Product Sales — Monthly")
plt.xlabel("Product")
plt.ylabel("Units Sold")
plt.tight_layout()
plt.show()
