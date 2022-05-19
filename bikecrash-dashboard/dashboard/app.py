from functools import reduce
from typing import Any, Dict, List, Tuple
import dash_bootstrap_components as dbc
from matplotlib.pyplot import margins
import numpy as np
import plotly.express as px
import plotly.graph_objects as go
from dash import Dash, Input, Output, dash_table, dcc, html
from components.static import navbar
from components.filtering import bike_year_slider, ambulance_checklist
from data.external import bikecrash_df, filter_bikecrash, filter_bikecrash_by_selection
from graphs.templates import bar_traficcontrol, bar_speedlimit, histogram_injury


app = Dash(__name__, external_stylesheets=[dbc.themes.BOOTSTRAP])


app.layout = html.Div(
    [
        navbar,
        
            html.Br(),
            dbc.Row([
                dbc.Col(html.Span("Year slider:"), width=2, style={'font-weight' :  'bold'}),
                dbc.Col(bike_year_slider(), width=6),
                dbc.Col(html.Span("Ambulance slider:"), width=2, style={'font-weight' :  'bold'}),
                dbc.Col(ambulance_checklist(), width=2)
            ], style={'margin': 20}),
            
            dbc.Row([ 
                dbc.Col(id="bar-traficcontrol-col",children=bar_traficcontrol(), width=4),
                dbc.Col(id="bar-speedlimit-col", children=bar_speedlimit(), width=4),
                dbc.Col(id="histogram-injury-col", children=histogram_injury(), width =4)
            ], style={'margin': 20}
            ),
            html.Br(),
            dbc.Row([
                dbc.Col(
                    dash_table.DataTable(
                        data=bikecrash_df().to_dict("records"),
                        columns=[{"name": i, "id": i} for i in bikecrash_df().columns],
                        page_action="native",
                        page_current=0,
                        page_size=8,
                        id="bikecrash-table"
                    )
                )
            ], style={'margin': 20}),
            html.Br(),
        
    ]
)

@app.callback(
    Output("bar-traficcontrol-col", "children"),
    Output("bar-speedlimit-col", "children"),
    Output("histogram-injury-col", "children"),
    Input("bike-year-slider", "value"),
    Input("ambulance-checklist", "value"),
    prevent_initial_call=True
)
def adjust_main_graphs(
    year_range: List[float], ambulance_list: List[str] ) -> Tuple[dcc.Graph,dcc.Graph,dcc.Graph]:
    return (
        bar_traficcontrol(year_range, ambulance_list),
        bar_speedlimit(year_range, ambulance_list), 
        histogram_injury(year_range, ambulance_list),
    )

@app.callback(
    Output("bikecrash-number-field", "children"),
    Output("bikecrash-table", "data"),
    Input("bike-year-slider", "value"),
    Input("ambulance-checklist", "value"),
    Input("bar-traficcontrol", "selectedData"),
    Input("bar-speedlimit", "selectedData"),
)
def adjust_textual_data(  
    year_range: List[float], 
    ambulance_list: List[str], 
    traficcontrol_selection, 
    speedlimit_selection,
) -> Tuple[str,Dict[str,Any]]:
    df = bikecrash_df()
    df = filter_bikecrash(df, year_range, ambulance_list)
    df = filter_bikecrash_by_selection(df, traficcontrol_selection, speedlimit_selection)
    bikecrash_count = len(df)
    bikecrash_count_text = f"Number of accidents: {bikecrash_count}" 
    return bikecrash_count_text , df.to_dict("records")


if __name__ == "__main__":
    app.run_server(
        port=8062,
        debug=True,
        dev_tools_hot_reload=True,
        dev_tools_hot_reload_max_retry=5,
        dev_tools_hot_reload_interval=5,
    )
