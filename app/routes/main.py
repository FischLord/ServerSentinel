from flask import Blueprint, render_template, request
from app.tools.serverRequestsIPMI import *

bp_main = Blueprint('main', __name__)

# Hello world message

@bp_main.route('/')
def hello():
    return 'Hello World!'