import plotly.express as px
import plotly.offline as pyo

df = px.data.tips()
fig = px.bar(df, x="sex", y="total_bill", color="smoker", barmode="group")

# fig.show()
pyo.plot(fig,filename='bar_plot_ex.html')