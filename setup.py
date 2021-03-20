from setuptools import setup, find_packages

with open('requirements.txt') as file:
    requirements = file.readlines()

long_desc = 'Package for running map-reduce jobs on WIW public data sets.'

setup(
    name='MapReduceWIW',
    version='1.0.0',
    author='Bhairav Valera',
    author_email='bhairavvalera98@gmail.com',
    url='https://github.com/BhairavValera/MapReduceWIW',
    description='WIW public data map-reduce job package',
    long_description=long_desc,
    long_description_content_type="text/markdown",
    license='MIT',
    packages=find_packages(),
    entry_points={
        'console_scripts': [
            'MapReduceWIW=MapReduceWIW.main:main'
        ]
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent"
    ],
    install_requires=requirements,
    zip_safe=False
)