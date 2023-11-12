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

register_page(__name__, path="/viewer", icon="fa-solid:home")

def layout(file_id=None, **other_unknown_query_strings):

    return dmc.Container(
        children=[dmc.Text('Page with results')
        ],
        pt=20,
        style={"paddingTop": 20},
        size="98%",
    )