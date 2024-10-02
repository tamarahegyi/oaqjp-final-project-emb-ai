from setuptools import setup, find_packages
from flask import Flask

setup(
    name='EmotionDetection',
    version='1.0.0',
    description='A Python package for emotion detection using Watson NLP',
    packages=find_packages(),
    install_requires=[
        'requests'
    ],
)