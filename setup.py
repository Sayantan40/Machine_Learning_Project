## Importing the necessary libraries
from setuptools import setup
from typing import List
from setuptools import find_packages

## Declaring variables for setup function.
PROJECT_NAME = "Housing-Price-Predictor"
VERSION = "0.0.1"
AUTHOR = "Sayantan Mitra"
DESCRIPTION = "This is a regression Machine Learning Project"
PACKAGES = find_packages()
REQUIREMENT_FILE_NAME = "requirements.txt"
HYPHEN_E_DOT = "-e ."


## This function is going to read the requirements.txt file
## And then it is going to return list(name) from that as string value.
def get_requirements_list()->List[str]:

    """
    Description : This function is going to return a list of libraries(name) as string values mentioned in the requirements.txt file.
    Description: This function is going to return list of requirement
    mention in requirements.txt file
    return This function is going to return a list which contain name
    of libraries mentioned in requirements.txt file
    
    """
    
    with open(REQUIREMENT_FILE_NAME) as requirement_file:
        
        requirement_list = requirement_file.readlines()
        
        requirement_list = [requirement_name.replace("\n", "") for requirement_name in requirement_list]
        
        if HYPHEN_E_DOT in requirement_list:
            
            requirement_list.remove(HYPHEN_E_DOT)
        
        return requirement_list


setup(
    
    name = PROJECT_NAME,
    version = VERSION ,
    author = AUTHOR ,
    description = DESCRIPTION ,
    packages = PACKAGES ,
    install_requires = get_requirements_list()
    
    
    )
     
