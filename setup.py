from setuptools import  find_packages,setup
from typing import  List

Hyphen_e_dot  = '-e .'
def get_requirements(file_path:str)-> List[str]:
    with open(file_path, 'r') as f:
        requirements = f.readlines()
        requirements = [req.strip().replace('\n','') for req in requirements]
        if Hyphen_e_dot in requirements:
            requirements.remove(Hyphen_e_dot)

    return requirements


setup(

## https://packaging.python.org/en/latest/guides/distributing-packages-using-setuptools/

    name = 'Smoking detection ml project',
    author = 'Satyam',
    author_email = 'codexistslonglastingnotfog@gmail.com',
    packages = find_packages(),
    install_requires = get_requirements('requirements.txt')
)