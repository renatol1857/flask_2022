"""
Projeto HelloWrld em Flask
By Renato Leme
"""

from flask import Flask

__version__='0.0.1'

app = Flask(__name__)

from . import routes



