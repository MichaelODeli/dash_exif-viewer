from dash import (
    dcc,
    html,
    Input,
    Output,
    callback,
    register_page,
    State,
    Input,
    Output,
    no_update,
)
import dash_mantine_components as dmc

register_page(__name__, path="/guide", icon="fa-solid:home")

def layout(**other_unknown_query_strings):

    return dmc.Container(
        children=[dmc.Text('Help page')
        ],
        pt=20,
        style={"paddingTop": 20},
        size="98%",
    )