#install all the requirement to local packages wherever needed, we don't 
#have to install it separately in virtual environment

from setuptools import find_packages,setup

setup(
    name="mcqgenerator",
    version="0.0.1",
    author="vasudha21",
    author_email="vasudha.mishra10@outlook.com",
    install_requires=["openai","langchain","streamlit","python-dotenv","PyPDF2"],
    packages=find_packages()
)