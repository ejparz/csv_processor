import pandas as pd

class FormatterSvc(object):

    def __init__(self):
        ""

    def formatCategoryColumn(self, df: pd.DataFrame):
        ""

        df["Category"] = df["Category"].apply(lambda x: "Boomer was here" if x == "Boomer" else x)
        return df