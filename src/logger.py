import logging
import os
import sys

# create directory for logs
log_dirs = "logs"
log_filepath = os.path.join(log_dirs, "running_logs.log")
os.makedirs(log_dirs, exist_ok=True)

# Configure the logging settings
logging.basicConfig(
    level=logging.INFO,
    format='-------------------Execution starts------------------\nFile name - %(filename)s\nAt - %(asctime)s\nModule name - %(module)s\nAt line %(lineno)d\nError level - %(levelname)s\nMessage - %(message)s\n-------------------Execution Ends------------------',
    handlers=[
        logging.FileHandler(log_filepath),  ## for writing log in the file
        logging.StreamHandler(sys.stdout)  ## for terminal
    ]
)
# our custom logger
logger = logging.getLogger(name='Smoking ml main')
