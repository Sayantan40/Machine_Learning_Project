
## Importing the necessary libraries/modules
from distutils.log import INFO
import logging
from datetime import datetime
import os
import pandas as pd
from housing.constant import get_current_time_stamp


## Creating the logging directory/folder
LOG_DIR = "housing_logs"
os.makedirs(LOG_DIR,exist_ok=True)

## get current time stamp
CURRENT_TIME_STAMP = f"{datetime.now().strftime('%Y-%m-%d_%H-%M-%S')}"

## Creating the logging file name
LOG_FILE_NAME = f"log_{CURRENT_TIME_STAMP}.log"

## path/destination of the logging file
LOG_FILE_PATH = os.path.join(LOG_DIR,LOG_FILE_NAME)

# Create and configure logger
logging.basicConfig(
    
    filename=LOG_FILE_PATH,
    format="[%(asctime)s] %(name)s - %(levelname)s - %(message)s" ,
    filemode='w',
    level=logging.INFO
    
    )


def get_log_dataframe(file_path):
    
    data=[]
    
    with open(file_path) as log_file:
        
        for line in log_file.readlines():
            
            data.append(line.split("^;"))

    
    log_df = pd.DataFrame(data)
    
    columns=["Time stamp","Log Level","line number","file name","function name","message"]
    
    log_df.columns=columns
    
    log_df["log_message"] = log_df['Time stamp'].astype(str) +":$"+ log_df["message"]

    return log_df[["log_message"]]


def get_log_file_name():
    
    return f"log_{get_current_time_stamp()}.log"
 
