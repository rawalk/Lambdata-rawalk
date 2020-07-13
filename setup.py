# setup.py file

from setuptools import find_packages, setup

with open("README.md", "r") as fh:
    long_description = fh.read()

setup(
    name="lamdata_dspt6_rawalk",  # the name that you will install via pip
    version="1.0.1",
    author="Kush Rawal",
    author_email="kush-rawal@lambdastudents.com",
    description="2 helper utility functions",
    long_description=long_description,
    long_description_content_type="text/markdown",
    # required if using a md file for long desc
    # license="MIT",
    url="https://github.com/rawalk/Lambdata-rawalk",
    # keywords="",
    packages=find_packages()  # ["my_lambdata"]
)
