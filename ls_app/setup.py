from setuptools import setup

setup(
    name='ls_app',
    packages=['ls_app'],
    include_package_data=True,
    install_requires=[
        'flask',
        #TODO add nltk?
    ],
)
