import dash_bootstrap_components as dbc
from dash import html

bike_logo = "https://i.pinimg.com/originals/78/c4/24/78c42417cdcc474910f417d053bb606e.jpg"
navbar = dbc.Navbar(
    dbc.Container(
        [
            dbc.Row(
                [
                    dbc.Col(html.Img(src=bike_logo, height="60px")),
                    dbc.Col(dbc.NavbarBrand("Bicycle Collisions Dashboard", className="ms-2"))
                ],style={'font-weight' :  'bold'},
                align="center",
                className="g-0",
            ),
            html.Span(children=[], id="bikecrash-number-field", style={"color": "white"}),
            dbc.Button(
                "Reload",
                color="dark",
                className="me-1",
                href="/",
                external_link=True,
            ),
        ]
    ),
    color="primary",
    dark=True,
)
