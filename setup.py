# -*- coding: utf-8 -*-
from setuptools import find_packages, setup

with open("README.md", "r", encoding="utf-8") as f:
    readme = f.read()

requirements = [
    "tqdm"
]

extras = {
} #"nltk": ["nltk"],

setup(
    name="ttg",
    version="0.1-dev1",
    description="Thai Text Generator library",
    long_description=readme,
    long_description_content_type="text/markdown",
    author="Wannaphong Phatthiyaphaibun",
    author_email="wannaphong@kkumail.com",
    url="https://github.com/wannaphong/Thai-Text-Generator",
    packages=find_packages(),
    test_suite="tests",
    python_requires=">=3.6",
    package_data={
        "thaitextgenerator.corpus": [
        ],
    },
    install_requires=requirements,
    extras_require=extras,
    license="Apache Software License 2.0",
    zip_safe=False,
    keywords=[
        "NLP",
        "natural language processing",
        "text analytics",
        "text processing",
        "localization",
        "computational linguistics",
        "ThaiNLP",
        "Thai NLP",
        "Thai language",
    ],
    classifiers=[
        "Development Status :: 5 - Production/Stable",
        "Programming Language :: Python :: 3",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: Apache Software License",
        "Natural Language :: Thai",
        "Topic :: Scientific/Engineering :: Artificial Intelligence",
        "Topic :: Text Processing",
        "Topic :: Text Processing :: General",
        "Topic :: Text Processing :: Linguistic",
    ],
    project_urls={
    },
)