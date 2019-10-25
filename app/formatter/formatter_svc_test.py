import pandas as pd 
import unittest
from app.formatter.formatter_svc import FormatterSvc
import os

class TestLoadCsv(unittest.TestCase):
    def test_format_category(self):
        # initialize list of lists 
        data = [['Boomer', 10], ['Max', 15], ['Noodle', 14]] 
        
        # Create the pandas DataFrame 
        df = pd.DataFrame(data, columns = ['Category', 'Rating']) 

        formatterSvc = FormatterSvc()
        formattedDf = formatterSvc.formatCategoryColumn(df)
        
        print(df)
        self.assertEqual(formattedDf["Category"].iloc[0], "Boomer was here")
        self.assertEqual(formattedDf["Category"].iloc[1], "Max")
        self.assertEqual(formattedDf["Category"].iloc[2], "Noodle")
  
