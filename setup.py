#!usr/bin/env python3

try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

config = {
    'description': 'My flask portfolio app',
    'author': 'Bernard Asibu',
    'url': 'https://github.com/asibubernard/asibu_flask_portfolio',
    'download_url': 'https://github.com/asibubernard/asibu_flask_portfolio',
    'author_email': 'asibubernard@gmail.com',
    'version': '0.1',
    'install_requires': ['nose','flask'],
    'packages': ['asibu_flask_portfolio'],
    'scripts': [],
    'name': 'asibu_flask_portfolio'
        }

setup(**config)
