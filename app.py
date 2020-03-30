import dash
import dash_table
import dash_core_components as dcc
import dash_bootstrap_components as dbc
import dash_html_components as html
from dash.dependencies import Input, Output, State
import pandas as pd

external_stylesheets = [dbc.themes.BOOTSTRAP]

#create app
app = dash.Dash(__name__, external_stylesheets=external_stylesheets)

#read file
energy=pd.read_csv('https://opendata.maryland.gov/api/views/79zg-5xwz/rows.csv?accessType=DOWNLOAD')

# make a reuseable dropdown for the different examples
PLOTLY_LOGO="https://pics.clipartpng.com/midle/Renewable_Energy_PNG_Clipart-2976.png"


dropdown = dbc.DropdownMenu(
    children=[
        dbc.DropdownMenuItem("About"),
        dbc.DropdownMenuItem("Data Sets"),
        dbc.DropdownMenuItem(divider=True),
        dbc.DropdownMenuItem("Generation Capacity"),
        dbc.DropdownMenuItem("Energy Generated"),
    ],
    nav=True,
    in_navbar=True,
    label="Menu",
   
)

logo = dbc.Navbar(
    dbc.Container(
        [
            html.A(
                # Use row and col to control vertical alignment of logo / brand
                dbc.Row(
                    [
                        dbc.Col(html.Img(src=PLOTLY_LOGO, height="30px")),
                        dbc.Col(dbc.NavbarBrand("Renewable Energy In Maryland", className="ml-2")),
                    ],
                    align="center",
                    no_gutters=True,
                ),
                href="https://plot.ly",
            ),
            dbc.NavbarToggler(id="navbar-toggler"),
            dbc.Collapse(
                dbc.Nav(
                    [dropdown], className="ml-auto", navbar=True
                ),
                id="navbar-collapse",
                navbar=True,
            ),
        ]
    ),
    color="dark",
    dark=True,
    className="mb-5",
)


#call it into the display of the app
app.layout=html.Div([
    logo
])

def toggle_navbar_collapse(n, is_open):
    if n:
        return not is_open
    return is_open

app.callback(
        Output("navbar-collapse", "is_open"),
        [Input("navbar-toggler", "n_clicks")],
        [State("navbar-collapse", "is_open")],
    )(toggle_navbar_collapse)


if __name__ == '__main__':
    app.run_server(debug=True, port=1627)