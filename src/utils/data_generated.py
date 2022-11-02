'''
File containing functions for loading the generated data
'''

import pandas as pd

PATH_DATA_GEN = '../generated/'

FILENAME_ETHNICITIES = 'ethnicities'

def load_ethnicities():
    '''
    Load the ethnicities data.

    :return: data in dataframe
    '''
    return pd.read_pickle(PATH_DATA_GEN + FILENAME_ETHNICITIES)