'''
File containing functions for loading the generated data
'''

import pandas as pd

PATH_DATA_GEN = '../generated/'

FILENAME_ETHNICITIES = 'ethnicities'
FILENAME_MOVIE_METADATA = 'movie_metadata'
FILENAME_TITLE_CREW = 'title_crew'

def load_ethnicities() -> pd.DataFrame:
    '''
    Load the ethnicities data.

    :return: data in a dataframe
    '''
    return pd.read_pickle(PATH_DATA_GEN + FILENAME_ETHNICITIES)

def load_movie_metadata() -> pd.DataFrame:
    '''
    Load the movie metadata data.

    :return: data in a datafrmae
    '''
    return pd.read_pickle(PATH_DATA_GEN + FILENAME_MOVIE_METADATA)

def load_title_crew() -> pd.DataFrame:
    '''
    Load the title crew data.

    :return: data in a datafrmae
    '''
    return pd.read_pickle(PATH_DATA_GEN + FILENAME_TITLE_CREW)