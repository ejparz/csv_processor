from app.processor.processor_svc import Processor
from app.csv.csv_loader import CsvLoader

def main():
    p = Processor(CsvLoader())
    p.processCsv()