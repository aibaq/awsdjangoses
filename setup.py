from setuptools import (
    find_packages,
    setup,
)


setup(
    name='awsdjangoses',
    version='0.0.3',
    author='aibaq',
    description='Package for AWS SES bounces&complaints handling',
    url='https://github.com/aibaq/awsdjangoses',
    packages=find_packages(exclude=('*tests*',)),
    install_requires=[
        'django>=2.2',
        'djangorestframework>=3.11.0',
        'requests>=2.25.1',
    ],
    include_package_data=True,
    python_requires='>=3.6',
)
