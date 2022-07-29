import dash
from dash import html
from dash import dcc
from dash.dependencies import Input, Output


import pandas as pd

import plotly.graph_objects as go
import plotly.express as px

df = pd.read_csv("./data/penguins_size.csv")
df["sex"] = df['sex'].fillna(df['sex'].mode()[0])
df.iloc[:, 2:6] = df.iloc[:, 2:6].fillna(df.iloc[:, 2:6].mean())

print(df.head(5))
layout = html.Div(className="dashboard", children=[
    html.Div(className="graph graph-lg"),
    html.Div(className="graph"),
    html.Div(className="graph"),
    html.Div(className="graph"),
    html.Div(className="graph graph-md"),
    html.Div(className="graph graph-xl"),
    html.Div(className="graph graph-xl"),
    html.Div(className="graph graph-md")
])
