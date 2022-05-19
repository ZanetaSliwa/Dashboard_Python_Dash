from functools import reduce
import numpy as np
from dash import dcc
from data.external import bikecrash_df

def bike_year_slider() -> dcc.RangeSlider:
    df = bikecrash_df()
    year_min = df.CrashYear.min()
    year_max = df.CrashYear.max()
    return dcc.RangeSlider(year_min, year_max, 1, value=[2007, 2019], id='bike-year-slider', 
    marks={ 2007 : '2007',
            2008 : '2008',
            2009 : '2009',
            2010 : '2010',
            2011 : '2011',
            2012 : '2012',
            2013 : '2013',
            2014 : '2014',
            2015 : '2015',
            2016 : '2016',
            2017 : '2017',
            2018 : '2018',
            2019 : '2019'})


def ambulance_checklist() -> dcc.Checklist:
    checklist = dcc.Checklist(
        options=["Yes", "No"],
        value=["Yes", "No"],
        inline=True,
        id="ambulance-checklist"
    )
    return checklist




