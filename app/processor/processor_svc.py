
from app.file_svc.csv_svc import CsvSvc
from app.formatter.formatter_svc import FormatterSvc
import os

class ProcessorSvc(object):

    def __init__(self):
        self.csvSvc = CsvSvc()
        self.formatterSvc = FormatterSvc()
    
    def processCsv(self):

        currentDir = os.path.dirname(__file__)
        filePath = os.path.join(currentDir, '../../data/test_data.csv')

        data = self.csvSvc.getCsv(filePath)
        formatted = self.formatterSvc.formatCategoryColumn(data)

        filePathToWrite = os.path.join(currentDir, '../../test_data/processor_output.csv')
        self.csvSvc.writeDataFrameToCsv(formatted, filePathToWrite)

