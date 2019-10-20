import unittest
from app.csv.csv_loader import CsvLoader
import os

class TestLoadCsv(unittest.TestCase):
    def test_basic(self):
        self.assertEqual("hello", "hello")

    def test_load_csv(self):
        currentDir = os.path.dirname(__file__)
        filePath = os.path.join(currentDir, '../../data/test_data.csv')

        csvLoader = CsvLoader()
        data = csvLoader.getCsv(filePath)
        assert data != None


        


        