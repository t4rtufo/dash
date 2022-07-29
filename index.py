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

# Predictor sliders


@app.callback(Output('culmen_length', 'children'), [Input('culmen_length_input', 'value')])
def update_value(value):
    return f"Longitud del Pico ({round(float(value), 2)}mm)"


@app.callback(Output('culmen_depth', 'children'), [Input('culmen_depth_input', 'value')])
def update_value(value):
    return f"Ancho del Pico ({round(float(value), 2)}mm)"


@app.callback(Output('flipper_length', 'children'), [Input('flipper_length_input', 'value')])
def update_value(value):
    return f"Longitud de las aletas ({round(float(value), 2)}mm)"


@app.callback(Output('body_mass', 'children'), [Input('body_mass_input', 'value')])
def update_value(value):
    return f"Masa corporal ({round(float(value), 2)}kg)"

# Predictor radio


@app.callback(Output('female-label', 'className'), [Input('gender_radio', 'value')])
def update_options(value):
    return "female-label female-label-active" if(value == "female") else "female-label"


@app.callback(Output('male-label', 'className'), [Input('gender_radio', 'value')])
def update_options(value):
    return "male-label male-label-active" if(value == "male") else "male-label"


@app.callback(Output('torgersen-label', 'className'), [Input('island_radio', 'value')])
def update_options(value):
    return "torgersen-label torgersen-label-active" if(value == "torgersen") else "torgersen-label"


@app.callback(Output('dream-label', 'className'), [Input('island_radio', 'value')])
def update_options(value):
    return "dream-label dream-label-active" if(value == "dream") else "dream-label"


@app.callback(Output('biscoe-label', 'className'), [Input('island_radio', 'value')])
def update_options(value):
    return "biscoe-label biscoe-label-active" if(value == "biscoe") else "biscoe-label"


# Run the app on localhost:8050
if __name__ == '__main__':
    app.run_server(debug=True)
