import dash
from dash import dcc, html
import plotly.express as px
import pandas as pd

app = dash.Dash(__name__)

df = px.data.iris()

app.layout = html.Div(children=[
    html.H1(children='График распределения ирисов по видам'),
    
    dcc.Graph(
        id='scatter-plot',
        figure=px.scatter(df, x='sepal_width', y='sepal_length', 
                          color='species', title='Распределение ширины и длины чашелистиков')
    )
])

if __name__ == '__main__':
    app.run_server(debug=True)
