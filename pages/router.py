import dash

from dash import html


layout = html.Div(className="router", children=[
    html.H1(className="title", children="Archipiélago Palmer (Antártida)"),
    html.Div(className="pages-container",
             children=[
                 html.Div(className="page-card", children=[
                          html.Img(className="page-image",
                                   src="./assets/img/chart-icon.png"),
                          html.H2(className="page-title"),
                          html.A(className="page-link", href="/pages/dashboard",
                                 children=["Dashboard"])
                          ]),
                 html.Div(className="page-card", children=[
                          html.Img(className="page-image",
                                   src="./assets/img/penguin-icon.jpg"),
                          html.H2(className="page-title"),
                          html.A(className="page-link", href="/pages/prediction",
                                 children=["Predecir"])
                          ]),

             ]
             )
])
