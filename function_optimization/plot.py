import numpy as np
import matplotlib.pyplot as plt

def f(x):
    return x * np.sin(10*np.pi*x) + 1


x = np.linspace(-1, 2, 1000)
y = f(x)

plt.figure(figsize=(10, 5))
plt.plot(x, y, color='red')
plt.title("f(x) = x * sin(10πx) + 1")
plt.xlabel("x")
plt.ylabel("f(x)")
plt.grid(True)
plt.show()