from dash import Dash, dcc, html
from dash.dependencies import Output, Input, State
import dash_bootstrap_components as dbc

from model import process_image

app = Dash(__name__, external_stylesheets=[dbc.themes.BOOTSTRAP])


app.layout = dbc.Container(children=[
    dbc.NavbarSimple(brand="MNIST"),
    html.H1("Number classification", className="mt-5 mb-5"),
    dbc.Row([
        dbc.Col([dcc.Upload(id="input",
                            className="form-control-file",
                            style={"position": "absolute", "height": "38px", "width": "100%", "z-index": "2"}),
                 html.Label(
            "Your file...",
            id="label",
            htmlFor="input",
            className="custom-file-label")], width=10),
        dbc.Col(dbc.Button("Process", id="process_button", n_clicks=0,
                className="float-right", color="primary"), width=2)
    ]),
    html.Div(id="process_result")
])

@app.callback(
    Output(component_id="label", component_property="children"),
    Input(component_id="input", component_property="filename")
)
def change_placeholder(filename):
    if (filename):
        return filename
    else:
        return "Your file..."

@app.callback(
    Output(component_id='process_result', component_property='children'),
    State(component_id='input', component_property='contents'),
    Input(component_id="process_button", component_property='n_clicks')
)
def update_output_div( file, input_value):
    if (input_value>0):
        return process_image(file.split(',')[1])



if __name__ == '__main__':
    app.run_server(debug=True)
