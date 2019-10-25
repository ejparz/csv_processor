import unittest
from app.file_svc.csv_svc import CsvLoader
import os

class TestLoadCsv(unittest.TestCase):
    def test_basic(self):
        self.assertEqual("hello", "hello")

    def test_load_csv(self):
        currentDir = os.path.dirname(__file__)
        filePath = os.path.join(currentDir, '../../data/test_data.csv')

        csvLoader = CsvLoader()
        data = csvLoader.getCsv(filePath)
        self.assertTrue(len(data) > 10)


        


        