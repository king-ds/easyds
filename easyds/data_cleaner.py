import pandas as pd

def basic_clean(df, case=None):
    df = clean_columns(df)
    df = clean_rows(df)
    df = correct_dtypes(df)

    return df

def correct_dtypes(df):
    for i in df.columns:

        column = list(df[i])

        only_dates = [date for date in column if is_date(date)]
        date_percentage = (len(only_dates)/len(column)*100)

        only_integers = [number for number in column if str(number).isdigit()]
        int_percentage = (len(only_integers)/len(column)*100)

        # only_floats = [number for number in column if isinstance(number, float)]
        only_floats = [number for number in column if is_float(number)]
        float_percentage = (len(only_floats)/len(column)*100)

        if(date_percentage >= 80):
            df[i] = pd.to_datetime(df[i],errors='coerce')
        elif(int_percentage >= 80):
            df[i] = pd.to_numeric(df[i],errors='coerce')
        elif(float_percentage >= 80):
            df[i] = pd.to_numeric(df[i],errors='coerce')
        elif((int_percentage >= 60 and float_percentage >= 20) or (int_percentage >= 20 and float_percentage >=60)):
            df[i] = pd.to_numeric(df[i],errors='coerce')
        elif((int_percentage >= 30 and float_percentage >= 30) or (int_percentage >= 30 and float_percentage >=30)):
            df[i] = pd.to_numeric(df[i],errors='coerce') 
        elif(int_percentage >= 40 and float_percentage >= 40):
            df[i] = pd.to_numeric(df[i],errors='coerce')
        else:
            df[i] = df[i].astype('object')
        
    return df
import datetime


def is_date(string):
    boolean = []
    for fmt in ['%Y%m%d', '%Y-%m-%d', '%d.%m.%Y', '%d/%m/%Y', '%m/%d/%Y', '%Y/%m/%d']:
        try:
            datetime.datetime.strptime(string, fmt)
            boolean.append(True)
        except:
            boolean.append(False)
    if True in boolean:
        return True
    else:
        return False

def is_float(string):
    try:
        float(string)
        return True
    except:
        return False

def clean_columns(df):
    
    df.columns = df.columns.str.strip().str.lower().str.replace(' ', '_').str.replace('(', '').str.replace(')', '')
    return df

def clean_rows(df):
    """
    Remove associated whitespaces from the data.
    """
    columns = df.columns
    for column in columns:
        df[column] = df[column].apply(remove_whitespaces)
    return df

def remove_whitespaces(x):
    """
    helper function for clean_rows
    """
    if isinstance(x, str):        
        return x.strip()
    return x