import multiprocessing

bind = '0.0.0.0:8000'
workers = multiprocessing.cpu_count() * 2 + 1
max_requests = 10000
timeout = 45
name = 'dragalia'
