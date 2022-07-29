import dash

from dash import html
from dash import html, dcc
from dash.dependencies import Input, Output

# Connect to your app pages
from pages import prediction, dashboard, router


app = dash.Dash(__name__,

                external_stylesheets=[
                    {
                        'href': 'https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.1.2/css/all.min.css',
                        'rel': 'stylesheet',
                        'integrity': 'sha512-1sCRPdkRXhBV2PBLUdRb4tMg1w2YPf37qatUFeS7zlBy7jJI8Lf4VHwWfZZfpXtYSLy85pkm9GaYVYMfw5BC1A==',
                        'crossorigin': 'anonymous',

                    }
                ], suppress_callback_exceptions=True)

# Define the index page layout
app.layout = html.Div([
    dcc.Location(id='url', refresh=False), html.Div(
        id="page-content", children=[])
])

# Create the callback to handle mutlipage inputs


@app.callback(Output('page-content', 'children'), [Input('url', 'pathname')])
def display_page(pathname):
    if pathname == '/':
        return router.layout
    if pathname == '/pages/dashboard':
        return dashboard.layout
    if pathname == '/pages/prediction':
        return prediction.layout
    else:  # if redirected to unknown link
        return "404 Page Error! Please choose a link"

# Predictor


@app.callback(Output('culmen_length', 'children'), [Input('culmen_length_input', 'value')])
def update_value(value):
    return f"Longitud del Pico (mm) {round(float(value), 2)}"


# Run the app on localhost:8050
if __name__ == '__main__':
    app.run_server(debug=True)
