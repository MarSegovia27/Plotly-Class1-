import numpy as np
import plotly.graph_objs as go
import plotly.offline as pyo

np.random.seed(52)

random_x = np.random.randint(1,101,100)
random_y = np.random.randint(1,101,100)

# mi primer pedazo de información
trace1 = go.Scatter(x=random_x,y=random_y,mode='markers', name='Info 1')

# mi segundo pedazo de información
trace2 = go.Scatter(x=random_x,y=random_y+20,mode='markers', name='Info 2')

data = [trace1, trace2]

layout = go.Layout(
    title='Mi Plot',
    xaxis={'title':'Eje x'},
    yaxis=dict(title='Eje y'),
    hovermode='closest'
    )

fig = go.Figure(data=data,layout=layout)

pyo.plot(fig,filename='plotly_go_demo.html')

#https://plotly.com/python/