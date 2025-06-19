import yaml

data = {
    'jobs':[
        {
        'job_id': '1',
        'job_name': "transform csv",
        'tasks': [
            {
            'id': 1,
            'runner': 'readers.csv_reader.CsvReader',
            'params':r'file_path=C:\work\python_batch\batch\test\test1.csv;'
            },
            {
            'id': 2,
            'runner': 'transformers.dummy_transformer.CsvTransformer',
            },
            {
            'id': 3,
            'runner': 'writers.csv_writer.CsvWriter',
            'params':r'file_path=C:\work\python_batch\batch\test\test2.csv;'
            }
        ]
        },
        {
        'job_id': '2',
        'job_name': "dummy",
        'tasks': [
            {
            'id': 1,
            'runner': 'readers.csv_reader.CsvReader',
            'params':r'file_path=C:\work\python_batch\batch\test\test1.csv;'
            },
            {
            'id': 2,
            'runner': 'writers.csv_writer.CsvWriter',
            'params':r'file_path=C:\work\python_batch\batch\test\test2.csv;'
            }
        ]
        }

    ],

}

with open('config.yaml', 'w') as file:
    yaml.dump(data, file)