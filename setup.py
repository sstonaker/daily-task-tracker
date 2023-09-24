from setuptools import find_packages, setup

setup(
    name='daily-tracker',
    version='0.0.0',
    description="Daily tracker to track my activities.",
    author="Steven Stonaker",
    author_email="stevenstonaker@gmail.com",
    packages=find_packages(),
    install_requires=[
        'sqlalchemy==2.0.*',
        'fastapi==0.103.*',
        'uvicorn-0.23.2',
        'itsdangerous==2.1.*',
        'psycopg2==2.9.*',
        'jinja2==3.1.*',
    ]
)
