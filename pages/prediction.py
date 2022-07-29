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
                html.Img(src="../assets/img/default.png", id="penguin-image"),
                html.P(id="penguin-title", children="Nuevo Pingüino")
            ]),
            html.Div(className="sliders-container", children=[
                html.P(id="culmen_length", className="label",
                       children="Longitud del Pico (mm)"),
                html.Div(className="range-wrapper", children=[
                    html.Span(className="tag", children="30"),
                    dcc.Input(id="culmen_length_input",
                              type="range", min="30", max="60", value=45),
                    html.Span(className="tag", children="60")
                ]),

                html.P(id="culmen_depth", className="label",
                       children="Ancho del Pico (mm)"),
                html.Div(className="range-wrapper", children=[
                    html.Span(className="tag", children="15"),
                    dcc.Input(id="culmen_depth_input", type="range",
                              min="15", max="30", value=20),
                    html.Span(className="tag", children="30")
                ]),

                html.P(id="flipper_length", className="label",
                       children="Longitud de las Aletas (mm)"),
                html.Div(className="range-wrapper", children=[
                    html.Span(className="tag", children="170"),
                    dcc.Input(id="flipper_length_input", type="range",
                              min="170", max="220", value=195),
                    html.Span(className="tag", children="220")
                ]),

                html.P(id="body_mass", className="label",
                       children="Masa corporal (kg)"),
                html.Div(className="range-wrapper", children=[
                    html.Span(className="tag", children="2.5"),
                    dcc.Input(id="body_mass_input", type="range",
                              min="2.5", max="5", value=3),
                    html.Span(className="tag", children="5")
                ]),



                dcc.RadioItems(id="gender_radio", className="gender", options=[
                    {"label": html.Span(id="female-label", className="female-label", children=html.I(className="fa-solid fa-venus")),
                     "value": "female"},
                    {"label": html.Span(id="male-label", className="male-label", children=html.I(className="fa-solid fa-mars")),
                     "value": "male"}], value="female"),

                dcc.RadioItems(id="island_radio", className="island", options=[
                    {"label": html.Span(id="torgersen-label", className="torgersen-label", children="Torgersen"),
                     "value": "torgersen"},
                    {"label": html.Span(id="dream-label", className="dream-label", children="Dream"),
                     "value": "dream"},
                    {"label": html.Span(id="biscoe-label", className="biscoe-label", children="Biscoe"),
                     "value": "biscoe"}],
                    value="torgersen"),

                html.Button(type="button", id="predict-button", n_clicks=0,
                            children="Predecir especie")
            ])
        ]
    )
])
