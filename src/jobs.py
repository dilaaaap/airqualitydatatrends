from flask import Flask
import redis
import sys
import wget
import logging
import os

jobs = Flask(__name__)

