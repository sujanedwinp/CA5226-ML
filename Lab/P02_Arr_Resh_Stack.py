
import numpy as np

e_arr = np.round(np.linspace(0, 1, 10), 2)
imat = np.identity(3)
r_arr = np.reshape(e_arr, (2, 5))

a = np.array([1, 2, 3])
b = np.array([4, 5, 6])
vst = np.vstack((a,b))
hst= np.hstack((a,b))

print("Even Spaced:\n", e_arr)
print("Identity Mat:\n", imat)
print("Reshaped:\n", r_arr)
print(f"V-Stack:\n{vst}\nH-Stack:\n{hst}")