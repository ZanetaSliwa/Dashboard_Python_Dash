from functools import reduce
from typing import List
import numpy as np
import pandas as pd
import seaborn as sns


def bikecrash_df() -> pd.DataFrame:
    return pd.read_csv("C:/Users/Żaneta/pol/iwd/dashboard/bikecrash-dashboard/BikePedCrash4.csv", delimiter=";")


def filter_bikecrash(df: pd.DataFrame, year_range: List[float] = None, ambulance_list: List[str] = None) -> pd.DataFrame:
    if year_range is not None:
        df = df.loc[df.CrashYear.between(*year_range)]

    if ambulance_list is not None:
        df = df.loc[df.AmbulanceR.isin(ambulance_list)]
    return df


def filter_bikecrash_by_selection(df, traficcontrol_selection, speedlimit_selection):
    selections = []
    intersected_selection = None
    
    for selection in [traficcontrol_selection, speedlimit_selection]:
        if selection is not None:   
            selected_points = [point["pointIndex"] for point in selection["points"]]
            selections.append(selected_points)
    
    if len(selections) == 1:
        intersected_selection = selections[0]
        
    elif len(selections) > 1:
        intersected_selection = reduce(np.intersect1d, selections).tolist()
        
    if intersected_selection is not None:
        df = df.loc[df.index.isin(intersected_selection)]
    return df

