from setuptools import setup, find_packages

with open("README.md", "r") as fh:
    long_description = fh.read()

setup(
    name="Pytter2",
    version="0.0.1",
    author="M_Lbr",
    author_email="m.micky.lbr@gmail.com",
    description="Read write Twitter data with API v2",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/mlabarrere/Pytter2",
    packages=find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: Apache Software License",
        "Operating System :: OS Independent", "Natural Language :: English"
    ],
    install_requires=[
        'pygquery'
    ],
)
