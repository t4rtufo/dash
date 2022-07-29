import dash
from dash import html
from dash import dcc
from dash.dependencies import Input, Output


import pandas as pd

import plotly.graph_objects as go
import plotly.express as px


df = pd.read_csv("penguins_size.csv")

layout = html.Div([
    html.Div(
        className="prediction",
        children=[
            html.Div(className="penguin-container", children=[
                html.Img(id="penguin-image")
            ]),
            html.Div(className="sliders-container", children=[
                html.P(className="label", children="Longitud del Pico (mm)"),
                html.Div(className="range-wrapper", children=[
                    html.Span(className="tag", children="30"),
                    dcc.Input(className="", type="range", min="30", max="60"),
                    html.Span(className="tag", children="60")
                ]),

                html.P(className="label", children="Profundidad del Pico (mm)"),
                html.Div(className="range-wrapper", children=[
                    html.Span(className="tag", children="15"),
                    dcc.Input(type="range", min="15", max="30"),
                    html.Span(className="tag", children="30")
                ]),

                html.P(className="label", children="Longitud de las Aletas (mm)"),
                html.Div(className="range-wrapper", children=[
                    html.Span(className="tag", children="170"),
                    dcc.Input(type="range", min="170", max="220"),
                    html.Span(className="tag", children="220")
                ]),

                html.P(className="label", children="Masa corporal (kg)"),
                html.Div(className="range-wrapper", children=[
                    html.Span(className="tag", children="2.5"),
                    dcc.Input(type="range", min="2.5", max="5"),
                    html.Span(className="tag", children="5")
                ]),



                dcc.RadioItems(className="gender", options=[
                    {"label": html.I(className="fa-solid fa-venus"),
                     "value": "female"},
                    {"label": html.I(className="fa-solid fa-mars"),
                     "value": "male"}], value="female"),
                dcc.RadioItems(className="island", options=[
                    {"label": "Torgersen", "value": "torgersen"},
                    {"label": "Dream", "value": "dream"},
                    {"label": "Biscoe", "value": "biscoe"}],
                    value="torgersen"),
                html.Button(id="predict-button", children="Predecir especie")
            ])
        ]
    )
])
