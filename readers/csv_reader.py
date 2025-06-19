
from base.reader import Reader
import pandas as pd
import logging
logger = logging.getLogger(__name__)

class CsvReader(Reader):
    def run(self):
        logger.info('reading ...')
        params = self.params.split(';')
        file_path = params[0].split('=')
        file_path = file_path[1]
        logger.info(f'{self.task_id} reading {file_path} ...')
        df = pd.read_csv(file_path)
        self.job.data['csv_data']=df


