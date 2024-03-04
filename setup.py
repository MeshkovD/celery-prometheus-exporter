import os

from pip._internal.network.session import PipSession
from pip._internal.req import parse_requirements
from setuptools import find_packages, setup


def read_requirements(file_name):
    return [
        str(requirement) for requirement in
        parse_requirements(file_name, session=PipSession())
    ]


setup(
    name='celery-prometheus-exporter',
    version=os.getenv('SERVICE_VERSION', '1.0.0'),
    description='Prometheus exporter for celery metrics',
    author='Georgy Gritsenko',
    author_email='georgiy.gritsenko@techops.ru',
    packages=find_packages(exclude=('*.tests', 'tests.*')),
    include_package_data=True,
    classifiers=[
        'Programming Language :: Python :: 3.6',
    ],
    entry_points={
        'console_scripts': [
            'celery-exporter=celery_prometheus_exporter.main:main'
        ]
    },
    install_requires=[
        'flake8-print==3.0.1',
        'flake8==3.5.0',
        'pytest-cov==2.4.0',
        'pytest-mock==1.5.0',
        'pytest==3.4.2',
        'tox==2.9.1',
    ],
)
