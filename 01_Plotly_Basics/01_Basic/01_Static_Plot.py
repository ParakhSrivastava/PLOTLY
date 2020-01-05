#######
# "Static" matplotlib plot
######
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# create fake data:
df = pd.DataFrame(np.random.randn(100,4),columns='A B C D'.split())
# np.random.randn() ->  creates an array of specified shape and fills it with random values as per standard normal distribution

df.plot()
plt.show()
