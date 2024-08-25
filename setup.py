from setuptools import setup, find_packages

setup(
    name='renaming_script',
    version='1.0',
    packages=find_packages(),
    install_requires=[
        'PyPDF2',
        'colorama',
    ],
    entry_points={
        'console_scripts': [
            'renaming_script=main:process_folder',
        ],
    },
)
