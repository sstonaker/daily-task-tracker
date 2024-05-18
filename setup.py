from setuptools import find_packages, setup

setup(
    name='daily-tracker',
    version='0.0.0',
    description="Daily tracker to track my activities.",
    author="Steven Stonaker",
    author_email="stevenstonaker@gmail.com",
    packages=find_packages(),
    install_requires=[
        'pydantic==1.10.*',
        'fastapi==0.103.*',
        'uvicorn==0.23.*',
        'itsdangerous==2.1.*',
        'jinja2==3.1.*',
        'python-multipart==0.0.*',
        'sqlmodel==0.0.*',
    ]
)
