import traceback

import utils
import logging
logger = logging.getLogger(__name__)

import threading
from concurrent.futures import ProcessPoolExecutor
from base.job import Job

class JobRunner():

    lock = threading.Lock()
    executor:ProcessPoolExecutor =None

    def __init__(self):
        self._init_executor()

    def _init_executor(self):
        if JobRunner.executor is None:
            with JobRunner.lock:
                if JobRunner.executor is None:
                    JobRunner.executor = ProcessPoolExecutor(4)

    def run_job(self, job_id):
        try:
            from base.job_factory import JobInitilizer
            jobs = JobInitilizer.get_jobs()
            job = [job for job in jobs if job.job_id == str(job_id)]
            if len(job)==1:
                job=job[0]
                JobRunner.executor.submit(job.run)
            else:
                raise Exception(f'job {job_id} failed')
        except Exception as ex:
            logger.info(ex)
            traceback.print_exc()

    @staticmethod
    def shutdown():
        JobRunner.executor.shutdown()



def main():
    jobRunner = JobRunner()
    print(JobRunner.executor)
    jobRunner.run_job(job_id=1)
    jobRunner.run_job(job_id=2)

    import atexit
    def on_exit():
        logger.info('Existing Python process')
        JobRunner.shutdown()

    atexit.register(on_exit)

if __name__ == '__main__':
    main()