'''
File containing functions for loading the generated data
'''

import pandas as pd

PATH_DATA_GEN = '../generated/'
PATH_DATA_GEN_LEGACY = '../generated/legacy/'

FILENAME_ETHNICITIES = 'ethnicities'
FILENAME_MOVIE_METADATA = 'movie_metadata'
FILENAME_MOVIE_CREW = 'movie_crew'
FILENAME_MOVIE_PRINCIPALS = 'movie_principals'
FILENAME_MOVIE_RATINGS = 'movie_ratings'
FILENAME_PEOPLE = 'people'
FILENAME_IS_IN_MOVIES = 'is_in_movies'

def load_ethnicities() -> pd.DataFrame:
    '''
    Load the ethnicities data.

    :return: data in a dataframe
    '''
    return pd.read_pickle(PATH_DATA_GEN + FILENAME_ETHNICITIES)

def load_movie_metadata(legacy: bool = False) -> pd.DataFrame:
    '''
    Load the movie metadata data.

    :param legacy: load the legacy version of the data.
                   The legacy version differs only in that it contains
                   the entire timespan of the initial data.

    :return: data in a dataframe
    '''
    if legacy:
        path = PATH_DATA_GEN_LEGACY
    else:
        path = PATH_DATA_GEN
    return pd.read_pickle(path + FILENAME_MOVIE_METADATA)

def load_movie_crew() -> pd.DataFrame:
    '''
    Load the movie crew data.

    :return: data in a dataframe
    '''
    return pd.read_pickle(PATH_DATA_GEN + FILENAME_MOVIE_CREW)

def load_movie_principals() -> pd.DataFrame:
    '''
    Load the movie principals data.

    :return: data in a dataframe
    '''
    return pd.read_pickle(PATH_DATA_GEN + FILENAME_MOVIE_PRINCIPALS)

def load_movie_ratings() -> pd.DataFrame:
    '''
    Load the movie ratings data.

    :return: data in a dataframe
    '''
    return pd.read_pickle(PATH_DATA_GEN + FILENAME_MOVIE_RATINGS)

def load_people() -> pd.DataFrame:
    '''
    Load the people data.

    :return: data in a dataframe
    '''
    return pd.read_pickle(PATH_DATA_GEN + FILENAME_PEOPLE)

def load_is_in_movies() -> pd.DataFrame:
    '''
    Load the "is in movies" data.

    :return: data in dataframe
    '''
    return pd.read_pickle(PATH_DATA_GEN + FILENAME_IS_IN_MOVIES)