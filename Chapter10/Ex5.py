import matplotlib.pyplot as plt
import numpy as np

x = np.arange(0, 10, 1)

plt.subplot(1,2,1)
plt.plot(x, x*x)
plt.title("y=x^2")

plt.subplot(1,2,2)
plt.plot(x, np.sqrt(x))
plt.title("y=sqrt(x)")

plt.show()