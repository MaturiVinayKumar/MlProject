from setuptools import find_packages, setup

from typing import List

HYPEN_E_DOT='-e .'
def get_requirements(filepath)->List[str]:
    '''
    This function return all the list of requirements
    '''
    requirements=[]
    with open(filepath) as file_obj:
        requirements=file_obj.readlines()
        requirements=[req.replace("\n"," ") for req in requirements]
        if HYPEN_E_DOT in requirements:
            requirements.remove(HYPEN_E_DOT)


setup(
name='mlproject',
version=0.01,
author='Vinay',
author_email='Vinaykumar3414.maturi@gmail.com',
packages=find_packages(),
install_requires=get_requirements('requirements.txt')
)