import dash

from dash import html
from dash import html, dcc
from dash.dependencies import Input, Output, State
import plotly.express as px

import pandas as pd

from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
# from sklearn.metrics import classification_report,confusion_matrix

from pages import prediction, dashboard, router

# Recolección
df = pd.read_csv("./data/penguins_size.csv")

# Procesamiento
df["sex"] = df['sex'].fillna(df['sex'].mode()[0])
df = pd.get_dummies(df, columns=['sex', 'island'], drop_first=True)
df.iloc[:, 1:5] = df.iloc[:, 1:5].fillna(df.iloc[:, 1:5].mean())

scale = StandardScaler()
scale.fit(df.drop(['species'], axis=1))
transformed = scale.transform(df.drop(['species'], axis=1))
df_scaled = pd.DataFrame(transformed, columns=df.columns[1:])

# Entrenamiento
X = df_scaled
y = df['species']

x_train, x_test, y_train, y_test = train_test_split(X, y, test_size=0.25)

knn = KNeighborsClassifier(n_neighbors=3)

knn.fit(x_train, y_train)
out1 = knn.predict(x_test)


def predict(penguin):
    scaled_penguin = scale.transform(
        pd.DataFrame([penguin], columns=df.columns[1:]))
    transformed_penguin = pd.DataFrame(scaled_penguin, columns=df.columns[1:])
    species = knn.predict(transformed_penguin)

    return species[0]


penguins = pd.read_csv("./data/penguins_size.csv")
penguins["sex"] = penguins['sex'].fillna(penguins['sex'].mode()[0])
penguins.iloc[:, 2:6] = penguins.iloc[:, 2:6].fillna(
    penguins.iloc[:, 2:6].mean())
penguins["id"] = penguins.index + 1

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


@app.callback([Output('penguin-image', 'src'), Output('penguin-title', 'children')], [
    State('culmen_length_input', 'value'),
    State('culmen_depth_input', 'value'),
    State('flipper_length_input', 'value'),
    State('body_mass_input', 'value'),
    State('gender_radio', 'value'),
    State('island_radio', 'value'),
    Input('predict-button', 'n_clicks')
])
def update_penguin(culmen_length, culmen_depth, flipper, mass, gender, island, n_clicks):
    if(n_clicks == 0):
        return "../assets/img/default.png", "Nuevo Pingüino"

    new_penguin = [float(culmen_length), float(
        culmen_depth), float(flipper), float(mass)*1000]

    if(gender == "female"):
        new_penguin.extend([1, 0])
    else:
        new_penguin.extend([0, 1])

    if(island == "dream"):
        new_penguin.extend([1, 0])
    elif(island == "torgersen"):
        new_penguin.extend([0, 1])
    else:
        new_penguin.extend([0, 0])

    species = predict(new_penguin)
    return f"../assets/img/{species}.png", species

# Dashboard


@app.callback(Output('scatter-graph', 'figure'), [
    Input('dropdown-x', 'value'),
    Input('dropdown-y', 'value')
])
def update_scatter(x_value, y_value):
    return px.scatter(
        penguins, x=x_value, y=y_value, color="species",
        color_discrete_sequence=["orange", "purple", "green"],)


@app.callback(Output('lines-graph', 'figure'), [
    Input('dropdown-line', 'value')
])
def update_graph(value):
    return px.line(
        penguins, x="id", y=value, color="species",
        title=f"{value} según especie",
        color_discrete_sequence=["orange", "purple", "green"])


# Run the app on localhost:8050
if __name__ == '__main__':
    app.run_server(debug=True)
