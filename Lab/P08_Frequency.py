import matplotlib.pyplot as plt

data = (
    [12.5]*5 +
    [17.5]*6 +
    [22.5]*9 +
    [27.5]*8 +
    [32.5]*2
)

plt.hist(data, bins=[10,15,20,25,30,35], edgecolor="black")

plt.title("Histogram")
plt.xlabel("Class Interval")
plt.ylabel("Frequency")

plt.show()