import os, sys
import logging
import traceback
from abc import ABC, abstractmethod
logger = logging.getLogger(__name__)


class Task(ABC):

    def __init__(self):
        self.job = None
        self.task_id = None
        self.params = None

    def execute(self):
        logger.info(f'job {self.job.job_id} task {self.task_id} started ...')
        try:
            self.run()
        except Exception as ex:
            logger.info(f'job {self.job.job_id} task {self.task_id} failed')
            raise ex
        else:
            logger.info(f'job {self.job.job_id} task {self.task_id} finished')
    @abstractmethod
    def run(self):
        pass

    def set_job(self, job):
        self.job = job

    def set_taskID(self, task_id):
        self.task_id = task_id

    def set_params(self, params):
        self.params = params