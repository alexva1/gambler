import logging
from datetime import datetime
import os

current_datetime = datetime.now().strftime('%Y-%m-%d')
log_folder = 'src/logs'
log_filename = f'{current_datetime}.log'
log_file_path = os.path.join(log_folder, log_filename)

logging.basicConfig(
    level=logging.DEBUG,
    format='%(asctime)s : %(message)s',
    datefmt='%Y-%m-%d %H:%M:%S',
    handlers=[
        logging.FileHandler(log_file_path),  # Log to a file
    ]
)

logger = logging.getLogger()


__all__ = ['logger']
