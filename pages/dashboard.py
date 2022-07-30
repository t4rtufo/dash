from calendar import c
import dash
from dash import html
from dash import dcc
import plotly.express as px

import dash_daq as daq

import pandas as pd

import plotly.graph_objects as go
import plotly.express as px

penguins = pd.read_csv("./data/penguins_size.csv")
penguins["sex"] = penguins['sex'].fillna(penguins['sex'].mode()[0])
penguins.iloc[:, 2:6] = penguins.iloc[:, 2:6].fillna(
    penguins.iloc[:, 2:6].mean())
penguins["id"] = penguins.index + 1

gentoo_ratio = round(penguins[penguins["species"]
                              == "Gentoo"].size * 100 / penguins.size, 2)

chinstrap_ratio = round(penguins[penguins["species"]
                                 == "Chinstrap"].size * 100 / penguins.size, 2)

adelie_ratio = round(penguins[penguins["species"]
                              == "Adelie"].size * 100 / penguins.size, 2)

layout = html.Div(className="dashboard", children=[
    html.Div(className="graph penguins-amount graph-lg", children=[
        html.P(className="number", children=len(penguins)),
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
    html.Div(className="graph graph-xl scatter-graph",
             children=[dcc.Graph(id="scatter-graph",
                                 figure=px.scatter(
                                     penguins, x="culmen_length_mm", y="culmen_depth_mm", color="species",
                                     color_discrete_sequence=["orange", "purple", "green"])
                                 ),
                       html.Div(className="dropdowns-container", children=[
                           dcc.Dropdown(
                               options=[
                                {'label': 'Longitud del Pico',
                                    'value': 'culmen_length_mm'},
                                {'label': 'Ancho del Pico',
                                    'value': 'culmen_depth_mm'},
                                {'label': 'longitud de las Aletas',
                                    'value': 'flipper_length_mm'},
                                {'label': 'Masa Corporal', 'value': 'body_mass_g'}
                                ], value=penguins.columns[2], id='dropdown-x'),
                           dcc.Dropdown(
                               options=[
                                   {'label': 'Longitud del Pico',
                                       'value': 'culmen_length_mm'},
                                   {'label': 'Ancho del Pico',
                                    'value': 'culmen_depth_mm'},
                                   {'label': 'longitud de las Aletas',
                                    'value': 'flipper_length_mm'},
                                   {'label': 'Masa Corporal',
                                       'value': 'body_mass_g'}
                               ], value=penguins.columns[3], id='dropdown-y')

                       ])
                       ]
             ),
    html.Div(className="graph graph-xxl line-graph",
             children=[dcc.Graph(id="lines-graph",
                 figure=px.line(penguins, x="id", y="body_mass_g", color="species",
                       title='custom tick labels', color_discrete_sequence=["orange", "purple", "green"])
             ),
                 html.Div(className="dropdowns-container", children=dcc.Dropdown(
                     options=[
                         {'label': 'Longitud del Pico',
                          'value': 'culmen_length_mm'},
                         {'label': 'Ancho del Pico',
                          'value': 'culmen_depth_mm'},
                         {'label': 'longitud de las Aletas',
                          'value': 'flipper_length_mm'},
                         {'label': 'Masa Corporal',
                          'value': 'body_mass_g'}
                     ], value=penguins.columns[2], id='dropdown-line')
             )])
])
