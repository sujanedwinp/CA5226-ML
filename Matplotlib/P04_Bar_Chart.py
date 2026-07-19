import matplotlib.pyplot as plt

products = ["Laptop", "Phone", "Tablet", "Watch", "Headphones"]
sales    = [120, 350, 95, 210, 180]

plt.bar(products, sales, color=["blue", "red", "green", "yellow", "purple"])
plt.title("Product Sales")
plt.xlabel("Product")
plt.ylabel("Units Sold")
plt.tight_layout()
plt.show()
