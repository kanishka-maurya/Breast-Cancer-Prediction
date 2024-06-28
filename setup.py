from setuptools import find_packages,setup
from typing import List


HYPHEN_E_DOT = "-e ."
#my function will return a list.
def get_requirements(file_path:str)->List[str]:
    '''
    This function will return the list of required packages.
    '''
    requirements = []
    with open('requirements.txt') as file_obj:
        requirements = file_obj.readlines()
        requirements = [req.replace("\n"," ") for req in requirements.txt ]
        if HYPHEN_E_DOT in requirements:
            requirements.remove(HYPHEN_E_DOT)
    return requirements


setup(
    name = "ML_Project",
    version = "0.0.1",
    author = "Kanishka Maurya",
    author_email = "kanishkamauryaofficial@gmail.com",
    packages = find_packages(),
    install_requires = get_requirements("requirements.txt")
)