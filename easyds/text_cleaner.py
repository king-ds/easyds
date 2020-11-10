"""
Created on Thursday November 5 12:55 2020

@authors: king-ds
"""

import pandas as pd

def feature_extraction(df, column, stop_words):
    """
    Clean the corpus by eliminating special characters, numbers, one-two letter words,
    and stop words, and lowering the case for consistency. Returns the final dataframe
    including the transformed corpus.

    Parameters
    ----------
    df : dataframe object
         dataset
    column : string variable
         specify corpus column name
    stop_words : list
         collection of stop words

    """

    df['new_'+column] = df.apply(lambda x: run_helper_functions(x[column], stop_words), axis=1)
    return df

def remove_punctuations(x):

    punctuations = '''!()-[]{};:'"\,<>./?@#$%^&*_~`'''
    new_x = ''
    for char in x:
        if char not in punctuations:
            new_x = new_x + char
    return new_x

def remove_numbers(x):

    new_x = ''.join([i for i in x if not i.isdigit()])
    return new_x

def remove_stop_words(x, stop_words):

    new_x = [y for y in x.split() if y not in stop_words]
    #   new_x = " ".join(new_x)
    return new_x

def remove_one_two_letters(x):

    new_x = [y for y in x.split() if len(y) > 2]
    new_x = " ".join(new_x)
    return new_x

def lower_case(x):

    new_x = x.lower()
    return new_x

def run_helper_functions(x, stop_words):
    
    x = lower_case(x)
    x = remove_punctuations(x)
    x = remove_numbers(x)
    x = remove_one_two_letters(x)
    x = remove_stop_words(x, stop_words)
    return x