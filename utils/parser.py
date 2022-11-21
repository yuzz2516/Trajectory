import pandas as pd

def parser(text):   
    f = pd.read_csv(text, sep=' ')
    df = pd.DataFrame(f)
    df.columns = ['frame', 'ID', 'x', 'y', 'w', 'h', 'n1', 'n2', 'n3', 'n4', 'n5']
    df = df.drop(columns=["n1", "n2", "n3", "n4", "n5"])
    return df

def centerize(text):
    df = parser(text)
    y_list = df.loc[:,'y'].values
    x_list = df.loc[:,'x'].values
    w_list = df.loc[:,'w'].values
    h_list = df.loc[:,'h'].values

    xc_list = x_list + w_list / 2
    yt_list = y_list + h_list
    #print(df)
    return xc_list, yt_list
    