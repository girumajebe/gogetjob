# -*- coding: utf-8 -*-

import os
from datetime import datetime
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from job_func.job_search import job_search
from job_func.config import Config

app = Flask(__name__)
app.config.from_object(Config)
db = SQLAlchemy(app)

from job_func import routes
