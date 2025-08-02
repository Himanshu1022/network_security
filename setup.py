from setuptools import find_packages,setup
from typing import List

"""
The setup.py is the essential part of packaging and distributing the python project
"""
requirement_lst:list[str] = []
def get_requirement()->list[str]:
    try:
        with open ("requirements.txt","r") as file:
            lines = file.readlines()
            for line in lines:
                requirement = line.strip()

                if requirement and requirement != "-e .":
                    requirement_lst.append(requirement)
    except FileNotFoundError:
        print("file is not found")
    
    return requirement_lst
    
setup(
    name= "Network Security",
    version = "0.0.1",
    author= "Hiamnshu",
    author_email="piyushpatidar2210@gmail.com",
    packages=find_packages(),
    install_requires = get_requirement()



)