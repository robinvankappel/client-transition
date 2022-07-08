import pandas as pd; pd.set_option('display.width', 400); pd.set_option("display.max_columns", 8)
from utils import *

# import itertools
# import matplotlib.pyplot as plt
# from tqdm import trange, tqdm

def data_prep(DATA):
    """
    Convert custom data file with customer data from Excel to dataframes
    """
    # read file
    print(get_time(settings.time0), 'DATAFILE:', '\n')
    data = pd.read_excel(DATA, sheet_name=0, header=0)
    df_ref = pd.DataFrame(data) # make proper dataframe

    # improve dataframe
    print(get_time(settings.time0), 'Name:', DATA)
    print(get_time(settings.time0), 'Total clients:', len(df_ref))
    print(get_time(settings.time0), 'Total ARR (€):', round(df_ref.arr.sum(),2))
    return df_ref

# def get_unique_apps(df):
#     """
#     get unique Apps as sorted list
#     """
#     unique_apps = df['Apps'].explode().sort_values().unique()
#     unique_apps = list(filter(None, unique_apps))
#     print(get_time(settings.time0), 'apps used by clients:', '\n', unique_apps)
#     return unique_apps

def analyse_apps(df):
    """
    For all unique apps save how many clients use it and the related arr
    """
    apps = [col for col in df if col.startswith('App.')]
    print(get_time(settings.time0), 'apps used by clients:', '\n', apps)

    # count use per app and sum arr per app
    df_apps = pd.DataFrame(apps, columns=['unique_apps'])
    app_counter = list()
    app_arrs = list()
    for x in df_apps['unique_apps']:
        app_count = df[x].sum()
        app_counter.append(app_count)
        app_arr = (df[x]*df.arr).sum()
        app_arrs.append(app_arr)
    df_apps['app_counter'] = app_counter
    df_apps['app_arr'] = app_arrs

    return df_apps

def create_roadmap(roadmap_sequence, df_apps):
    roadmap = list()
    for i in roadmap_sequence:
        roadmap.append(df_apps.unique_apps[i])
    return roadmap
