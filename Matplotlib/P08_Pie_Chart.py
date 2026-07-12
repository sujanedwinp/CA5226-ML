import matplotlib.pyplot as plt

labels  = ["Python", "Java", "JavaScript", "C++", "Others"]
sizes   = [35, 25, 20, 12, 8]
colors  = ["steelblue", "tomato", "gold", "seagreen", "mediumpurple"]
explode = (0.05, 0, 0, 0, 0)   # slightly separate the largest slice

plt.pie(sizes, labels=labels, colors=colors, explode=explode,
        autopct="%1.1f%%", startangle=140)
plt.title("Programming Language Popularity")
plt.show()
