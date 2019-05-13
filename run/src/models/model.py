#!/usr/bin/env python3

from ..mappers.database import Database
import sqlite3

class User:

	def __init__(self,username):
		self.username = username

	def __enter__(self):
		return self

	def __exit__(self,type_,value,traceback):
		pass

	def user_id(self):
		with Database() as db:
			db.cursor.execute('''SELECT pk FROM users WHERE username="{}";'''.format(self.username))
			user_id = db.cursor.fetchone()[0]
			return user_id

	def login(self,password):
		with Database() as db:
			db.cursor.execute('''SELECT password FROM users WHERE username="{}";'''.format(self.username))
			stored_password = db.cursor.fetchone()[0]
			if password == stored_password:
				return True
			else:
				return False

	def signup(username,password):
		with Database() as db:
			db.cursor.execute('''SELECT username FROM users;''')
			usernames = db.cursor.fetchall()
			username_list = [i[0] for i in usernames]
			print(username_list)
			if username in username_list:
				return False
			else:
				db.cursor.execute('''INSERT INTO users(username,password) VALUES(?,?)''',(username,password))
				return True

	def homepage():
		with Database() as db:
			db.cursor.execute('''SELECT users.pk, users.username, posts.pk, posts.user_id, posts.time, posts.img,posts.caption FROM users, posts WHERE users.pk = posts.user_id ORDER BY time DESC;''')
			pots = db.cursor.fetchall()
		feed = [list(i) for i in pots]
		return feed

	def post(self,tm,img,caption):
		user_id = User.user_id(self)
		with Database() as db:
			db.cursor.execute('''INSERT INTO posts(user_id,time,img,caption) VALUES(?,?,?,?);''',(user_id,tm,img,caption))
		return True

	def repost(self,post_id,tm):
		user_id = User.user_id(self)
		with Database() as db:
			db.cursor.execute('''SELECT img,caption FROM posts WHERE pk={};'''.format(post_id))
			repost = db.cursor.fetchall()[0]
			db.cursor.execute('''INSERT INTO posts(user_id,time,img,caption) VALUES(?,?,?,?);''',(user_id,tm,repost[0],repost[1]))
		return True
