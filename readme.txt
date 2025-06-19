requires only create tasks, and add tasks in configuration

fastAPI
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
