import matplotlib.pyplot as plt

labels  = ["Python", "Java", "JavaScript", "C++", "Others"]
sizes   = [35, 25, 20, 12, 8]
colors  = ["blue", "red", "yellow", "green", "purple"]
explode = (0.05, 0, 0, 0, 0)

plt.pie(sizes, labels=labels, colors=colors, explode=explode)
plt.title("Piechart of Programming Languages")
plt.show()
