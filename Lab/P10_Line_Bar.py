
import matplotlib.pyplot as plt

time=[0, 1, 2, 3, 4, 5, 6]
speed=[0, 3, 7, 12, 20, 30, 45.6]

plt.plot(time, speed)
plt.title('Line Plot')
plt.show()

plt.bar(time, speed)
plt.title('Bar Plot')
plt.show()