# setup.py
from setuptools import setup, find_packages

setup(
    name="testdrive",                # PyPI name (must be all lowercase, no hyphens)
    version="0.1.0",                 # bump on each release
    author="Your Name",
    author_email="you@example.com",
    description="A simple Tkinter demo: Test Drive window",
    long_description=open("README.md", encoding="utf-8").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/YourUser/Test-Drive",  # update to your URL
    license="GPLv3",                 # since you chose GPLv3
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: GNU General Public License v3 (GPLv3)",
        "Operating System :: OS Independent",
    ],
    packages=find_packages(),        # automatically finds testdrive/
    python_requires=">=3.6",         # your minimum Python version
    install_requires=[],             # no external dependencies (tkinter is in stdlib)
    entry_points={
        "console_scripts": [
            "td=Testdrive.td:main"   # installs a `td` CLI that calls testdrive.td.main()
        ]
    },
)
