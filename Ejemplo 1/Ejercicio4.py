import numpy as np
import plotly.graph_objs as go
import plotly.offline as pyo

np.random.seed(52)

x_values = np.linspace(0,1,1000) #Punto de partida, punto final, steps
y_values = np.random.randn(1000)

new_y = np.sin(2*np.pi*x_values)

trace1 = go.Scatter(x= x_values, y= y_values, mode = 'lines', name = 'Data with lines')
trace2 = go.Scatter(x= x_values, y= y_values + 5, mode = 'markers', name = 'Data with markers')
trace3 = go.Scatter(x= x_values, y= y_values - 5, mode = 'lines+markers', name = 'Data wiith both')
trace4 = go.Scatter(x= x_values, y= new_y + 5, mode = 'lines', name = 'Sin func')

data = [trace1,trace2, trace3, trace4]

layout = go.Layout(
    title = 'My line plot',
    xaxis = dict(title = 'time'),
    yaxis = dict(title = 'something')
)

fig = go.Figure(data= data, layout = layout)

fig.show()
