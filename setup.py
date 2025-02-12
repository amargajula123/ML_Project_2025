from setuptools import setup
from typing import List


PROJECT_NAME="housing-predictor"
VERSION="0.0.1"
AUTHOR="Amar"
DESCRIPTION="This is the 2025 ML project"
PACKAGES=["housing"]
REQUIREMENT_FILE_NAME="requirements.txt"

def get_requirements_list()->List[str]:
    """Description: This function is goign to return list of 
    requiremets mentioned in requirements.txt file
    
    returns This function is going to return a list ,
    which contain name of libraries mentioned in the requirements.txt """
    with open(REQUIREMENT_FILE_NAME) as requirement_file:
        return requirement_file.readlines()
    


setup(
name=PROJECT_NAME,
version=VERSION,
author=AUTHOR,
description=DESCRIPTION,
packages=PACKAGES,

install_requires=get_requirements_list()



)

#if __name__=="__main__":
  #  print(get_requirements_list)