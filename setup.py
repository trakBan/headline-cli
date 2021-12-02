from setuptools import setup

setup(
   name='headline-cli',
   version='1.0',
   install_requires=["termcolor", "BeautifulSoup4"], 
   scripts=[
            'headline-cli',
           ]
)

