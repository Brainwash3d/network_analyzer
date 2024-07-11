from setuptools import setup, find_packages

setup(
    name='network_analyzer',
    version='0.1',
    packages=find_packages(),
    install_requires=[
        'requests',
        'psutil'
    ],
    entry_points={
        'console_scripts': [
            'network-analyzer=network_analyzer.analyzer:main',
        ],
    },
)
