from typing import List, Tuple
import plotly.express as px
from dash import dcc
from data.external import bikecrash_df, filter_bikecrash

def bar_traficcontrol(year_range: List[float] = None, ambulance_list: List[str] = None):
    
    _df = bikecrash_df()
    _df = filter_bikecrash(_df, year_range, ambulance_list)
    return dcc.Graph(id="bar-traficcontrol", figure= px.bar(data_frame=_df , x='CrashID', y='TraffCntrl', title="Types of checks/restrictions on the road"))

def bar_speedlimit(year_range: List[float] = None, ambulance_list: List[str] = None):
    _df = bikecrash_df()
    _df = filter_bikecrash(_df, year_range, ambulance_list)
    return dcc.Graph(id="bar-speedlimit", figure= px.bar(data_frame=_df , x='SpeedLimit', y='CrashID', title="Accidents with the speed limit on the road"))

def histogram_injury(year_range: List[float] = None, ambulance_list: List[str] = None):
    _df = bikecrash_df()
    _df = filter_bikecrash(_df, year_range, ambulance_list)
    return dcc.Graph(id="histogram-injury", figure= px.histogram(data_frame=_df , x='BikeInjury', nbins=20, title="The seriousness of the accident"))

