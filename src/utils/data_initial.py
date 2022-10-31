'''
File containing functions for loading the initial, unprocessed data
'''


import pandas as pd
import numpy as np

from utils.data_processing import map_to_nan, generate_dtype_map

CATEGORIES_GENDER = pd.CategoricalDtype(categories=['M', 'F'])
NA_VALUES_IMDB = ['\\N']

PATH_DATA = '../data/'

FOLDERNAME_CMU = 'cmu_movie_summary_corpus/'
FOLDERNAME_IMDB = 'imdb/'

COLUMNS_CMU_CHAR_METADATA = ['movie_id_wikipedia', 'movie_id_freebase', 'release_date', 'char_name', 'actor_bday', 'actor_gender',
                             'actor_height', 'actor_ethnicity', 'actor_name', 'actor_age_at_release', 'char_actor_map_id_freebase',
                             'char_id_freebase', 'actor_id_freebase']
COLUMNS_CMU_MOVIE_METADATA = ['movie_id_wikipedia', 'movie_id_freebase', 'movie_name',
                              'release_date', 'box_office_revenue', 'runtime', 'languages', 'countries', 'genres']
COLUMNS_CMU_NAME_CLUSTERS = ['char_name', 'char_actor_map_id_freebase']
COLUMNS_CMU_PLOT_SUMMARIES = ['movie_id_wikipedia', 'summary']
COLUMNS_CMU_TVTROPES_CLUSTERS = ['char_type', 'char_actor_map']

COLUMNS_IMDB_NAMES = ['person_name_id', 'person_name', 'birth_year',
                      'death_year', 'primary_profession', 'known_for_titles']
COLUMNS_IMDB_TITLE_BASICS = ['title_id', 'type', 'primary_title', 'original_title',
                             'is_adult', 'start_year', 'end_year', 'runtime_minutes', 'genres']
COLUMNS_IMDB_TITLE_CREW = ['title_id', 'directors', 'writers']
COLUMNS_IMDB_TITLE_RATINGS = ['title_id', 'average_rating', 'num_votes']

DTYPES_CMU_CHAR_METADATA = [int, pd.StringDtype(), object, pd.StringDtype(), object, CATEGORIES_GENDER, float, pd.StringDtype(
), pd.StringDtype(), pd.Int64Dtype(), pd.StringDtype(), pd.StringDtype(), pd.StringDtype()]
DTYPES_CMU_MOVIE_METADATA = [int, pd.StringDtype(
), pd.StringDtype(), object, float, float, object, object]
DTYPES_CMU_NAME_CLUSTERS = [pd.StringDtype(), pd.StringDtype()]
DTYPES_CMU_PLOT_SUMMARIES = [pd.StringDtype(), pd.StringDtype()]
DTYPES_CMU_TVTROPES_CLUSTERS = [pd.StringDtype(), object]

DTYPES_IMDB_NAMES = [pd.StringDtype(), pd.StringDtype(
), pd.Int16Dtype(), pd.Int16Dtype(), object, object]
DTYPES_IMDB_TITLE_BASICS = [pd.StringDtype(), pd.StringDtype(), pd.StringDtype(
), pd.StringDtype(), pd.Int32Dtype(), pd.Int32Dtype(), pd.Int32Dtype(), object, object]
DTYPES_IMDB_TITLE_CREW = [pd.StringDtype(), object, object]
DTYPES_IMDB_TITLE_RATINGS = [
    pd.StringDtype(), pd.Float32Dtype(), pd.Int32Dtype()]


def load_cmu_character_metadata():
    '''
    Load character metadata from the cmu dataset.
    Does the preliminary data cleaning.

    :return: data in dataframe
    '''
    dtype_map = generate_dtype_map(
        COLUMNS_CMU_CHAR_METADATA, DTYPES_CMU_CHAR_METADATA)
    path = PATH_DATA + FOLDERNAME_CMU + 'character.metadata.tsv'

    df = pd.read_csv(path, sep='\t', header=None,
                     names=COLUMNS_CMU_CHAR_METADATA)

    # data cleaning
    df.release_date.replace("1010-12-02", "2010-12-02", inplace=True)
    map_to_nan(df, 0, ['actor_age_at_release'])

    df = df.astype(dtype_map)
    df.release_date = pd.to_datetime(df.release_date)
    df.actor_bday = pd.to_datetime(df.actor_bday, errors='coerce')

    return df


def load_cmu_movie_metadata():
    '''
    Load movie metadata from the cmu dataset.
    Does the preliminary data cleaning.

    :return: data in dataframe
    '''
    dtype_map = generate_dtype_map(
        COLUMNS_CMU_MOVIE_METADATA, DTYPES_CMU_MOVIE_METADATA)
    path = PATH_DATA + FOLDERNAME_CMU + 'movie.metadata.tsv'

    df = pd.read_csv(path, sep='\t', header=None,
                     names=COLUMNS_CMU_MOVIE_METADATA, type=dtype_map)

    # data cleaning
    df.release_date.replace("1010-12-02", "2010-12-02", inplace=True)
    map_to_nan(df, 0, ['runtime'])

    df.release_date = pd.to_datetime(df.release_date)

    return df


def load_cmu_name_clusters():
    '''
    Load the name cluster data from the cmu dataset.
    Does the preliminary data cleaning.

    :return: data in dataframe
    '''
    dtype_map = generate_dtype_map(
        COLUMNS_CMU_NAME_CLUSTERS, DTYPES_CMU_NAME_CLUSTERS)
    path = PATH_DATA + FOLDERNAME_CMU + 'name.clusters.txt'

    df = pd.read_csv(path, sep='\t', header=None,
                     names=COLUMNS_CMU_NAME_CLUSTERS, dtype=dtype_map)

    return df


def load_cmu_tvtropes_clusters():
    '''
    Load the tvtropes clusters data from the cmu dataset.
    Does the preliminary data cleaning.

    :return: data in dataframe
    '''
    dtype_map = generate_dtype_map(
        COLUMNS_CMU_TVTROPES_CLUSTERS, DTYPES_CMU_TVTROPES_CLUSTERS)
    path = PATH_DATA + FOLDERNAME_CMU + 'tvtropes.clusters.txt'

    df = pd.read_csv(path, sep='\t', header=None,
                     names=COLUMNS_CMU_TVTROPES_CLUSTERS, dtype=dtype_map)

    return df


def load_imdb_name_basics():
    '''
    Load the name basics data from the imdb dataset.
    Does the preliminary data cleaning.

    :return: data in dataframe
    '''
    dtype_map = generate_dtype_map(COLUMNS_IMDB_NAMES, DTYPES_IMDB_NAMES)
    path = PATH_DATA + FOLDERNAME_IMDB + 'name.basics.tsv.gz'

    df = pd.read_csv(path, sep='\t', skiprows=1, names=COLUMNS_IMDB_NAMES,
                     dtype=dtype_map, na_values=NA_VALUES_IMDB, low_memory=False)

    return df


def load_imdb_title_basics():
    '''
    Load the title basics data from the imdb dataset.
    Does the preliminary data cleaning.

    :return: data in dataframe
    '''
    dtype_map = generate_dtype_map(
        COLUMNS_IMDB_TITLE_BASICS, DTYPES_IMDB_TITLE_BASICS)
    path = PATH_DATA + FOLDERNAME_IMDB + 'title.basics.tsv.gz'

    df = pd.read_csv(path, sep='\t', skiprows=1, names=COLUMNS_IMDB_TITLE_BASICS,
                     na_values=NA_VALUES_IMDB, dtype=dtype_map, low_memory=False)

    # data cleaning
    badvals = ['Reality-TV', 'Talk-Show', 'Documentary',
               'Game-Show', 'Animation,Comedy,Family', 'Game-Show,Reality-TV']
    df.runtime_minutes = df.runtime_minutes.map(
        lambda r: np.NaN if r in badvals else r).astype(pd.Int64Dtype())
    map_to_nan(df, 0, ['runtime_minutes'])

    return df


def load_imdb_title_crew():
    '''
    Load the title crew data from the imdb dataset.
    Does the preliminary data cleaning.

    :return: data in dataframe
    '''
    dtype_map = generate_dtype_map(
        COLUMNS_IMDB_TITLE_CREW, DTYPES_IMDB_TITLE_CREW)
    path = PATH_DATA + FOLDERNAME_IMDB + 'title.crew.tsv.gz'

    df = pd.read_csv(path, sep='\t', skiprows=1, names=COLUMNS_IMDB_TITLE_CREW,
                     dtype=dtype_map, na_values=NA_VALUES_IMDB)

    return df


def load_imdb_title_rating():
    '''
    Load the title ratings data from the imdb dataset.
    Does the preliminary data cleaning.

    :return: data in dataframe
    '''
    dtype_map = generate_dtype_map(
        COLUMNS_IMDB_TITLE_RATINGS, DTYPES_IMDB_TITLE_RATINGS)
    path = PATH_DATA + FOLDERNAME_IMDB + 'title.ratings.tsv.gz'

    df = pd.read_csv(path, sep='\t', skiprows=1, names=COLUMNS_IMDB_TITLE_RATINGS,
                     dtype=dtype_map, na_values=NA_VALUES_IMDB)

    return df
