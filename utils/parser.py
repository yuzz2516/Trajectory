import pandas as pd

def parser(text):   
    f = pd.read_csv(text, sep=' ')
    df = pd.DataFrame(f)
    df.columns = ['frame', 'ID', 'x', 'y', 'w', 'h', 'n1', 'n2', 'n3', 'n4', 'n5']
    df = df.drop(columns=["n1", "n2", "n3", "n4", "n5"])
    return df

    