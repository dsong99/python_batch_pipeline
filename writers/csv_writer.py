
from base.writer import Writter
import pandas as pd

class CsvWriter(Writter):
    def write(self):
        params = self.params.split(';')
        file_path = params[0].split('=')
        file_path = file_path[1]
        if 'csv_data' in self.job.data.keys():
            data_df = self.job.data['csv_data']
            data_df.to_csv(file_path)

