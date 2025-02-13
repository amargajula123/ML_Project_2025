from setuptools import setup,find_packages
from typing import List


PROJECT_NAME="housing-predictor"
VERSION="0.0.4"
AUTHOR="Amar"
DESCRIPTION="This is the 2025 ML project"
REQUIREMENT_FILE_NAME="requirements.txt"

def get_requirements_list()->List[str]:
    """Description: This function is goign to return list of 
    requiremets mentioned in requirements.txt file
    
    returns This function is going to return a list 
    which contain name of libraries mentioned in the requirements.txt """
    with open(REQUIREMENT_FILE_NAME) as requirement_file:
        return requirement_file.readlines()#.remove("-e .")
    


setup(
name=PROJECT_NAME,
version=VERSION,
author=AUTHOR,
description=DESCRIPTION,

packages=find_packages(),
install_requires=get_requirements_list()
)
# find_packages() will search all the packages that you are created and its going to return that names