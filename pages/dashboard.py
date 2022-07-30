import dash
from dash import html
from dash import dcc
import dash_daq as daq

from dash.dependencies import Input, Output


import pandas as pd

import plotly.graph_objects as go
import plotly.express as px

penguins = pd.read_csv("./data/penguins_size.csv")
penguins["sex"] = penguins['sex'].fillna(penguins['sex'].mode()[0])
penguins.iloc[:, 2:6] = penguins.iloc[:, 2:6].fillna(
    penguins.iloc[:, 2:6].mean())

gentoo_ratio = round(penguins[penguins["species"]
                              == "Gentoo"].size * 100 / penguins.size, 2)

chinstrap_ratio = round(penguins[penguins["species"]
                                 == "Chinstrap"].size * 100 / penguins.size, 2)

adelie_ratio = round(penguins[penguins["species"]
                              == "Adelie"].size * 100 / penguins.size, 2)

layout = html.Div(className="dashboard", children=[
    html.Div(className="graph penguins-amount graph-lg", children=[
        html.P(className="number", children=penguins.size),
        html.P(className="title", children="Pingüinos registrados")
    ]),
    html.Div(className="graph species-graph",
             children=[daq.Gauge(id='gentoo-graph', label="GENTOO", value=gentoo_ratio,
                                 max=100, color="green", scale={'start': 0, 'interval': 50, 'labelInterval': 2}),
                       html.P(className="ratio-label", children=f"{gentoo_ratio}%")]),

    html.Div(className="graph species-graph",
             children=[daq.Gauge(id='chinstrap-graph', label="CHINSTRAP", value=chinstrap_ratio,
                                 max=100, color="purple", scale={'start': 0, 'interval': 50, 'labelInterval': 2}),
                       html.P(className="ratio-label", children=f"{chinstrap_ratio}%")]),

    html.Div(className="graph species-graph",
             children=[daq.Gauge(id='adelie-graph', label="ADÉLIE", value=adelie_ratio,
                                 max=100, color="orange", scale={'start': 0, 'interval': 50, 'labelInterval': 2}),
                       html.P(className="ratio-label", children=f"{adelie_ratio}%")]),

    html.Div(className="graph graph-md", children=dcc.Graph(
        figure={
            'data': [
                {'x': ["Macho", "Hembra"], 'y': [65, 58],
                    'type': 'bar', 'name': 'Gentoo',
                    'marker': {"color": "green"}
                 },
                {'x': ["Macho", "Hembra"], 'y': [34, 34],
                    'type': 'bar', 'name': 'Chinstrap',
                    'marker':{"color": "purple"}},
                {'x': ["Macho", "Hembra"], 'y': [79, 73],
                    'type': 'bar', 'name': u'Adélie',
                    'marker':{"color": "orange"}},
            ],
            'layout': {
                'title': 'Sexo por especies'
            }
        }
    )),
    html.Div(className="graph graph-xl",children=dcc.Graph(
        
    )),
    html.Div(className="graph graph-xl"),
    html.Div(className="graph graph-md")
])
