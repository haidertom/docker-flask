from flask import Flask
import logging as logger
logger.basicConfig(level="DEBUG")

flask_app_instance = Flask(__name__)

from api import tasks