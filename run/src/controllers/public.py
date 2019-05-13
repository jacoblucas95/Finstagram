#!/usr/bin/env python3

from flask import Blueprint,request,render_template,redirect,session

from src.models.model import User

controller = Blueprint('public',__name__)


@controller.route('/',methods=['GET','POST'])
def homepage():
	if request.method == 'GET':
		tweets = User.homepage()
		return render_template('home.html',i=tweets)

@controller.route('/login',methods=['GET','POST'])
def login():
	if request.method == 'GET':
		return render_template('login.html')
	elif request.method == 'POST':
		username = request.form['username']
		password = request.form['password']
		with User(username) as u:
			if u.login(password):
				session['username'] = username
				return redirect('/')
			else:
				return redirect('/signup')

@controller.route('/signup',methods=['GET','POST'])
def signup():
	if request.method == 'GET':
		return render_template('signup.html')
	elif request.method == 'POST':
		username = request.form['username']
		password = request.form['password']
		if User.signup(username,password):
			session['username'] = username
			return redirect('/')
		else:
			return redirect('/login')
