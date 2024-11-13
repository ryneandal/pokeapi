import os
from multiprocessing import cpu_count

bind = f'0.0.0.0:{os.environ.get("SERVER_PORT", "80")}'
workers = cpu_count() * 2
threads = cpu_count() * 2
