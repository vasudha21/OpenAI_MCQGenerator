import logging
import os
from datetime import datetime

#define name of log file based on timestamp
LOG_FILE=f"{datetime.now().strftime('%m_%d_%Y_%H_%M_%S')}.log"

#location to store logs, i.e. in current working directory
log_path=os.path.join(os.getcwd(),"logs")

#pass path to make directory method to make the folder
os.makedirs(log_path,exist_ok=True)

#inside folder create .log file
LOG_FILEPATH=os.path.join(log_path,LOG_FILE)

#create object of this logging file with info level, filename and format
logging.basicConfig(level=logging.INFO, 
        filename=LOG_FILEPATH,
        format="[%(asctime)s] %(lineno)d %(name)s - %(levelname)s - %(message)s"
)
