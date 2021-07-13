import plotly.graph_objs as go

sent = ['긍정', '부정', '중립']
value = [87, 11, 3]
data = [go.Pie(
    labels=sent,
    values=value,
    pull=[0, 0, 0]
)]
fig = go.Figure(data=data)
fig.show()
