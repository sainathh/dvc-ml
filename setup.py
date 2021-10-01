from setuptools import setup

with open("README.md", "r", encoding="utf-8") as f:
    long_description = f.read()

setup(
    name="src",
    version="0.0.1",
    author="Sainadh",
    description="A Small Package for dvc ml pipeline poc",
    Long_description=long_description,
    Long_description_content_type="text/markdown",
    url="https://github.com/sainathh/dvc-ml.git",
    author_email="sainadh.potta@gmail.com",
    packages=["src"],
    python_requires=">=3.7",
    install_requires=[
        'dvc',
        'pandas',
        'scikit-learn'
    ]
)