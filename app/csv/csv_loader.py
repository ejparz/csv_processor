import pandas as pd

class CsvLoader(object):

    def __init__(self):
        ""
    
    def getCsv(self, path: str):
        return pd.read_csv(path, encoding ='latin1') 
    
    def writeDataFrameToCsv(self, df: pd.DataFrame, path: str):
        df.to_csv(path)