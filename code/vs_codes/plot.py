import datetime
import matplotlib.pyplot as plt
import numpy as np

xpoint = np.random.rand(1000)
ypoint = np.random.rand(1000)

# plt.plot(xpoint,ypoint)
plt.scatter(xpoint,ypoint)

# plt.savefig(f'{datetime.datetime.now()}.png')
plt.show()