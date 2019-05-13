#!/usr/bin/env python3

from flask import Flask,session

from .controllers.public import controller as public_controller
from .controllers.private import controller as private_controller

omnibus = Flask(__name__)

def keymaker(application):
	application.config['SECRET_KEY'] = 'opensesame'
	return application

keymaker(omnibus)

omnibus.register_blueprint(public_controller)
omnibus.register_blueprint(private_controller)
