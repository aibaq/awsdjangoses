from setuptools import setup


setup(
    name='awsdjangoses',
    version='0.0.1',
    author='aibaq',
    description='Package for AWS SES bounces&complaints handling',
    url='https://github.com/aibaq/awsdjangoses',
    install_requires=['django>=2.2', 'djangorestframework>=3.11.0', 'requests>=2.25.1'],
    include_package_data=True,
    python_requires='>=3.6',
)
