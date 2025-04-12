import pandas as pd

def carregarDados():
    df = pd.read_csv('../data/unicorns-till-sep-2022.csv')
    return df