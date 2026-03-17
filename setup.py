from setuptools import setup, find_packages

setup(
    name="CalendarGenerator",
    version="0.1.0",
    packages=find_packages(),
    install_requires=[
        "pandas",
        "holidays",
        "datetime"
    ],
    author="Taaps",
    description="Gerador de calendários com feriados Brasileiros"
)