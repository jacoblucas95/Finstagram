#!/usr/bin/env python3

from flask import Blueprint,request,render_template,redirect,session
from src.models.model import User
import os,time

UPLOAD_FOLDER = '/Users/jacoblucas/insta'

controller = Blueprint('private',__name__)

APP_ROOT = os.path.dirname(os.path.abspath(__file__))

tm = time.time()

@controller.route('/upload',methods=['GET','POST'])
def post():
	if request.method == 'GET':
		return render_template('test_post.html')
	elif request.method == 'POST':
		if session:
			username = session['username']
			caption = request.form['caption']

			target = os.path.join(APP_ROOT, '../static')

			for file in request.files.getlist('file'):
				filename = file.filename
				print(filename)
				destination = '/'.join([target, filename])
				file.save(destination)

				if User(username).post(tm,filename,caption):
					return redirect('/')



@controller.route('/repost',methods=['POST'])
def repost():
	if request.method == 'GET':
		pass
	elif request.method == 'POST':
		if session:
			username = session['username']
			post_id = request.form['post_id']
			if User(username).repost(post_id,tm):
				return redirect('/')
		else:
			return redirect('/login')

@controller.route('/logout')
def logout():
	session.pop('username')
	return redirect('/')