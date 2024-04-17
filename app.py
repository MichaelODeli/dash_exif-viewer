import dash
from dash import dcc, html, Output, Input, State, clientside_callback
import dash_mantine_components as dmc
from dash_iconify import DashIconify
import dash_bootstrap_components as dbc

app = dash.Dash(
    __name__,
    use_pages=True,
    external_stylesheets=[dbc.themes.ZEPHYR, dbc.icons.FONT_AWESOME],
)

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
                "EXIF Viewer",
                href="/",
                className="h3 me-5",
                style={"textDecoration": "none"},
            ),
            dbc.NavbarToggler(id="navbar-toggler", n_clicks=0), 
            dbc.Collapse(
                children=[
                    dmc.Grid(
                        [
                            dmc.Col(
                                html.A(
                                    "Инструкция",
                                    href="/guide",
                                    style={
                                        "text-decoration": "none",
                                        "font-size": '1rem'
                                    },
                                ),
                                span="content",
                            ),
                            dmc.Col(span="auto"),
                            dmc.Col(
                                html.Span(
                                    [
                                        dbc.Label(
                                            className="fa fa-moon",
                                            html_for="color-mode-switch",
                                            color="primary",
                                        ),
                                        dbc.Switch(
                                            id="color-mode-switch",
                                            value=True,
                                            className="d-inline-block ms-1",
                                            persistence=True,
                                        ),
                                        dbc.Label(
                                            className="fa fa-sun",
                                            html_for="color-mode-switch",
                                            color="primary",
                                        ),
                                    ]
                                ),
                                span="content",
                            ),
                        ],
                        className='grid-padding',
                        style={'min-width': '100%'}
                    )
                ],
                id="navbar-collapse",
                is_open=False,
                navbar=True,
            ),
        ]
    ),
    class_name='rounded border-bottom',
    color='default',
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


clientside_callback(
    """
    (switchOn) => {
       document.documentElement.setAttribute('data-bs-theme', switchOn ? 'light' : 'dark');  
       return window.dash_clientside.no_update
    }
    """,
    Output("color-mode-switch", "id"),
    Input("color-mode-switch", "value"),
)

if __name__ == "__main__":
    app.run_server(debug=True, host="0.0.0.0", port=82)
