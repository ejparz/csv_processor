import unittest
from app.processor.processor_svc import ProcessorSvc

from app.file_svc.csv_svc import CsvSvc
import os


class TestLoadCsv(unittest.TestCase):
    def test_process(self):
		print(self)
        p = ProcessorSvc()
        p.processCsv()
        
        currentDir = os.path.dirname(__file__)
        filePath = os.path.join(currentDir, '../../test_data/processor_output.csv')

        csvLoader = CsvSvc()
        data = csvLoader.getCsv(filePath)

        print(data)
        self.assertTrue(len(data) > 10)

 