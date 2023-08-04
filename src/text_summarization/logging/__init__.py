import os
import sys
import logging


logging_str = '[%(asctime)s: %(levelname)s: %(module)s: %(message)s]'
log_dir = 'logs'
log_filepath = os.path.join(log_dir, 'running_logs.log')
os.makedirs(log_dir, exist_ok=True)

logging.basicConfig(
    format= logging_str, 
    level=logging.INFO,
    handlers = [
        logging.FileHandler(log_filepath),
        logging.StreamHandler(sys.stdout)
    ]
)

logger = logging.getLogger('text-summarizer-logger')