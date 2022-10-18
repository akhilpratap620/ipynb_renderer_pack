import os
import sys
import logging

logging_str = "[%(asctime)s: %(levelname)s]: %(message)s"
log_dir = "./logs"
log_file_path = os.path.join(log_dir ,"running_log.log")

os.makedirs(log_dir, exist_ok= True)

logging.basicConfig(level=logging.INFO , format=logging_str, handlers=[
    logging.StreamHandler(sys.stdout),
    logging.FileHandler(log_file_path),
])

logger= logging.getLogger("IPYNBrenderer")
