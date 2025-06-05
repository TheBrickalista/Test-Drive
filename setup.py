# setup.py

from setuptools import setup, find_packages

setup(
    name="test_drive",        # this can be anything lowercase
    version="0.1.0",          # bump this on each real release
    packages=find_packages(), # finds any Python packages (folders with __init__.py)
    install_requires=[],      # list any dependencies, or leave empty
    author="Your Name",
    author_email="you@example.com",
    description="A simple Tkinter demo package", 
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: GNU General Public License v3 (GPLv3)",
        "Operating System :: OS Independent",
    ],
)
