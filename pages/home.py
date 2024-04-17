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
)
import dash_mantine_components as dmc
import base64

register_page(__name__, path="/", icon="fa-solid:home", name="EXIF Viewer")

layout = dmc.Container(
    children=[
        dmc.Stack(
            [
                html.H4("Просмотрщик EXIF данных в фотографиях."),
                dcc.Markdown(
                    """EXIF означает **«Высокоэффективный формат файла изображения»**.   
                             Это стандарт хранения полезных метаданных для цифровых файлов изображений,   
                             который поддерживает запись множества технических сведений —   
                             от времени и даты создания изображения до выбранных камеры, объектива и параметров съемки.""",
                    style={"text-align": "center"},
                ),
                dcc.Markdown(
                    "С помощью этого приложения вы можете просмотреть эти данные в фотографии. После просмотра данных файл будет удален с наших серверов. "
                ),
                html.Div(
                    [
                        dcc.Upload(
                            id="upload-data",
                            children=html.Div(
                                [
                                    "Перетащите или ",
                                    html.A(
                                        "выберите файлы",
                                        className="font-weight-bold",
                                        style={"textDecoration": "none"},
                                    ),
                                ]
                            ),
                            style={
                                "width": "100%",
                                "height": "60px",
                                "lineHeight": "60px",
                                "borderWidth": "1px",
                                "borderStyle": "dashed",
                                "borderRadius": "5px",
                                "textAlign": "center",
                                "margin": "10px",
                            },
                            # Allow multiple files to be uploaded
                            multiple=False,
                            max_size=50000000,
                            accept='image/*'
                        ),
                        html.Div(id="output-data-upload"),
                    ]
                ),
            ],
            align="center",
            justify="center",
        )
    ],
    pt=20,
    style={"padding": "20px", "min-width": "100%", "min-height": "100%"},
)


@callback(
    Output("output-data-upload", "children"),
    Input("upload-data", "contents"),
    State("upload-data", "filename"),
    State("upload-data", "last_modified"),
    prevent_initial_call=True,
)
def update_output(list_of_contents, list_of_names, list_of_dates):
    if list_of_contents is not None:
        extension = list_of_names.split('.')[-1]
        filetype = list_of_contents.split(';')[0]
        content = list_of_contents.split(',')[-1].encode()

        with open(f"imgs/user_image.{extension}", "wb") as fh:
            fh.write(base64.decodebytes(content))
        children = f""
        return children
