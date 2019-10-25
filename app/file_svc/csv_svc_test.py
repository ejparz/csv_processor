import unittest
from app.file_svc.csv_svc import CsvSvc
import os

class TestLoadCsv(unittest.TestCase):
    def test_load_csv(self):
        print(self)
        currentDir = os.path.dirname(__file__)
        filePath = os.path.join(currentDir, '../../data/test_data.csv')

        csvLoader = CsvSvc()
        data = csvLoader.getCsv(filePath)

        print(data)
        self.assertTrue(len(data) > 10)


        


        