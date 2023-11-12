import dash
from dash import dcc, html, Output, Input, State
import dash_mantine_components as dmc
from dash_iconify import DashIconify
import dash_bootstrap_components as dbc

app = dash.Dash(__name__, use_pages=True, external_stylesheets=[dbc.themes.BOOTSTRAP])

server = app.server
app.config.suppress_callback_exceptions = True


def get_icon(icon):
    return dmc.ThemeIcon(
        DashIconify(icon=icon, width=18),
        size=30,
        radius=30,
        variant="subtle",
    )

navbar = dbc.Navbar(
    dbc.Container(
        [
            html.A(
                # Use row and col to control vertical alignment of logo / brand
                "EXIF Viewer",
                href="/",
                className="h3 me-5",
                style={"textDecoration": "none", "color": "black"},
            ),
            dbc.NavbarToggler(id="navbar-toggler", n_clicks=0),
            dbc.Collapse(
                children=[
                    dbc.Row(
                        [
                            dbc.Col(
                                dbc.DropdownMenuItem("Instruction",href="https://example.com"),
                            ),
                            dbc.Col(width="auto"),
                            dbc.Col(
                                dbc.DropdownMenuItem("Support",href="https://example.com"),
                            ),
                        ]
                    )
                ],
                id="navbar-collapse",
                is_open=False,
                navbar=True,
            ),
        ]
    ),
    color="light",
    # dark=True,
)


# Конструкция всего макета
app.layout = html.Div(children=[navbar, dash.page_container])


# add callback for toggling the collapse on small screens
@app.callback(
    Output("navbar-collapse", "is_open"),
    [Input("navbar-toggler", "n_clicks")],
    [State("navbar-collapse", "is_open")],
)
def toggle_navbar_collapse(n, is_open):
    if n:
        return not is_open
    return is_open


if __name__ == "__main__":
    app.run_server(debug=True, host="0.0.0.0", port=8050)
