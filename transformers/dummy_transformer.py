import utils
from base.transformer import Transformer

import logging
logger = logging.getLogger(__name__)

class CsvTransformer(Transformer):
    def tranform(self):
        if 'csv_data' in self.job.data.keys():
            data_df = self.job.data['csv_data']
            data_df.drop(columns='A', inplace=True)
            self.job.data['csv_data'] = data_df
