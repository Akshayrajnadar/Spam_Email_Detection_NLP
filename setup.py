from setuptools import setup, find_packages
from typing import List

E_DOT="-e ."
def get_requirements(file_path:str) -> List[str]:
    requirements = []
    with open(file_path, 'r') as f:
        requirements = f.readlines()
        [req.replace('\n', '') for req in requirements]

        if E_DOT in requirements:
            requirements.remove(E_DOT)
    
    return requirements

setup(
    name='Email Spam Detection',
    version='0.0.1',
    author='akshayraj',
    packages=find_packages(),
    install_requires=get_requirements('requirements.txt'),
)