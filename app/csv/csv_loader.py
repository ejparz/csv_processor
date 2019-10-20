import pandas as pd

class CsvLoader(object):

    def __init__(self):
        ""
    
    def getCsv(self, path: str):
        return pd.read_csv(path) 