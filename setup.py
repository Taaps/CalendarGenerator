from setuptools import setup, find_packages

setup(
    name="CalendarGenerator",
    version="0.1.1",
    packages=find_packages(),
    install_requires=[
        "pandas",
        "holidays",
        "datetime",
        'numpy'
    ],
    author="Taaps",
    description="Gerador de calendários com feriados Brasileiros"
)