import logging
from base.job import Job
import threading
logger = logging.getLogger(__name__)
class JobInitilizer(object):
    jobs = None
    lock = threading.Lock()

    @staticmethod
    def _init_job():
        JobInitilizer.jobs = []
        config_path = r'./../utils/config.yaml'
        import yaml
        logger.info('initializing Jobs ...')
        config = None
        with open(config_path, 'r') as file:
            config = yaml.safe_load(file)

        config_jobs = config['jobs']
        for job_desc in config_jobs:
            job = Job(job_desc)
            JobInitilizer.jobs.append(job)

    @staticmethod
    def get_jobs():
        if JobInitilizer.jobs is None:
            with JobInitilizer.lock:
                if JobInitilizer.jobs is None:
                    JobInitilizer._init_job()
        return JobInitilizer.jobs



