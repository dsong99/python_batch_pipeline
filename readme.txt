A mini Python Batch Pipeline framewrok, it requires only create jobs, tasks, and add them in configuration either in a text file like yaml or defined in a dadtabase table. 
In case to monitor the batch processes, a DB logger can be created, which will insert a status record in a DB table, then add db_logger at the beging and end of each task, better to do this in taask wrappers, like reader, writer and performer. 

fastAPI (A job can be triggered in FastApi webserice)
    start -> initJobs from configurations or DB
    receives a request -> construct a job -> submit to job executor

Job_factory:
    init jobs objects from configuration

Job_runner:
    int a process pool executor, run_job method submits a job object to process executor

A POC demo:
    job_runner main method creates two jobs:
    job1 reader read a csv, tranformer remove 1 column, writer write result to a csv
    job2 simply print a line in reader and writer
