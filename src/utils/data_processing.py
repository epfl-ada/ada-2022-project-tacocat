'''
File containing functions useful for data processing and cleaning
'''

import pandas as pd
import numpy as np

SOME_CONSTANT = 0

def map_to_nan(df: pd.DataFrame, val: any, columns: list[str]):
    '''
    Map values of columns to NaN.

    :param df: Dataframe
    :param val: the value to map
    :param columns: columns of the dataframe to modify
    '''
    for col in columns:
        df[col] = df[col].map(lambda x: np.NaN if x ==
                              val else x, na_action='ignore')

def generate_dtype_map(columns: list[str], dtypes: list[type]) -> dict:
    '''
    Generate the dictionnary to change dataframe data types.

    :param columns: column names
    :param dtypes: data types

    :return: dictionnary mapping clumn name to data type
    '''
    assert len(columns) == len(dtypes)

    return {col: dtype for col, dtype in zip(columns, dtypes)}
