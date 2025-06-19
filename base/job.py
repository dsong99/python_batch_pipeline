import utils
import os, sys

import logging
logger = logging.getLogger(__name__)
import traceback

class Job(object):
    def __init__(self,job_desc:dict):
        self.job_desc = job_desc
        self.job_id = job_desc['job_id']
        self.job_name = job_desc['job_name']
        self.tasks_desc = job_desc['tasks']
        self.tasks = []
        self._create_tasks()
        self.status = 'None'
        self.data = {}
        self.job_desc.update({'status':self.status})

    def set_job_param(self, params):
        self.job_param = params

    def get_job_state(self):
        self.job_desc['status'] = self.status
        return self.job_desc

    def run(self):
        logger.info(f'running job {self.job_id} {self.job_name}')
        try:
            logger.info(f'total tasks {len(self.tasks)}')
            for task in self.tasks:
                task.execute()
        except Exception as ex:
            logger.info(f'job {self.job_id} failed with {str(ex)}')
            traceback.print_exc()
            self.status = 'FAILED'
        else:
            self.status='SUCCESS'
        logger.info(f'job {self.job_id} {self.status}')

    def _create_tasks(self):
        logger.info(f'create tasks {str(self.tasks_desc)}')
        for task_desc in self.tasks_desc:
            logger.info(f'create task_des {str(task_desc)}')
            runner = task_desc['runner']
            last_dot = runner.rfind('.')
            module_name = runner[:last_dot]
            class_name = runner[last_dot + 1:]
            logger.info(f'module {module_name}, class {class_name}')
            try:
                import importlib
                md = importlib.import_module(module_name)
                cls=getattr(md, class_name)
                task = cls()
            except Exception as ex:
                logger.info('Error creating task')
                traceback.print_exc()
                raise Exception(ex)
            logger.info(f'task {type(task)} setting params')
            task.set_job(self)
            task.set_taskID(task_desc['id'])
            if 'params' in task_desc.keys():
                task.set_params(task_desc['params'].strip())
            logger.info(f'task {task.task_id} {type(task)} is crated successfully')
            self.tasks.append(task)

        logger.info(f'job {self.job_id} {self.job_name} create tasks finished, total tasks {len(self.tasks)}')

    def __str__(self):
        return str(self.job_desc)