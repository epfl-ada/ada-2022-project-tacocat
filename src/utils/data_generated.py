'''
File containing functions for loading the generated data
'''

import pandas as pd

PATH_DATA_GEN = '../generated/'

FILENAME_ETHNICITIES = 'ethnicities'
FILENAME_MOVIE_METADATA = 'movie_metadata'

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