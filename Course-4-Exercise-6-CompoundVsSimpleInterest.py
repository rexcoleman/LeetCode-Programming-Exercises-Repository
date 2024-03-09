import matplotlib.pyplot as plt
import numpy as np

plt.xlabel('$n$')
plt.ylabel('Money ($)')

x = np.arange(200)
plt.plot(x, 1.02 ** x, label='$1.02^n$')
plt.plot(x, 1.02 * x, label='1 + 1.02^n')
plt.legend(loc='upper left')
plt.savefig('Course-4-Exercise-6.png')
