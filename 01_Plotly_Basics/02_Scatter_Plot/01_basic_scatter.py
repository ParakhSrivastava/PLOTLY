#######
# This plots 100 random data points (set the seed to 42 to
# obtain the same points we do!) between 1 and 100 in both
# vertical and horizontal directions.
######

import plotly.offline as pyo
import plotly.graph_objs as go
import numpy as np

np.random.seed(42)
# to get same random values

random_x = np.random.randint(1,101,100)
random_y = np.random.randint(1,101,100)
# generating Random Dataset

data = [go.Scatter(x = random_x,y = random_y,mode = 'markers',)]
# mode for marker points in Scatter Plot
# 'data' is the object created for Scatter Plot

pyo.plot(data, filename='scatter1.html')
# plotting with specific name of file
# always creates .HTML file
