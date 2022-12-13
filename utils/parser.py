import pandas as pd
import numpy as np

def parser(text):   
    f = pd.read_csv(text, sep=' ')
    df = pd.DataFrame(f)
    df.columns = ['frame', 'ID', 'x', 'y', 'w', 'h', 'n1', 'n2', 'n3', 'n4', 'n5']
    df = df.drop(columns=["n1", "n2", "n3", "n4", "n5"])
    return df

def parser_byte(text):
    f = pd.read_csv(text, sep=',')
    df = pd.DataFrame(f)
    df.columns = ['frame', 'ID', 'x', 'y', 'w', 'h', 'n1', 'n2', 'n3', 'n4']
    df = df.drop(columns=["n1", "n2", "n3", "n4"])
    return df

def centerize(df):
    x_min = df['x']
    y_min = df['y']
    w = df['w']
    h = df['h']

    x_c = x_min + w / 2
    y_t = y_min + h

    x_c = x_c.to_numpy()
    y_t = y_t.to_numpy()
    y_t = y_t.astype(int)
    return x_c, y_t
    
def xy_array(x, y):
    xy = np.stack([x, y], -1)
    return xy
    
