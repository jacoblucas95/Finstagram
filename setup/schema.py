#!/usr/bin/env python3

import sqlite3

connection = sqlite3.connect('setup/insta.db',check_same_thread=False)
cursor = connection.cursor()

#Users table
cursor.execute(
	'''CREATE TABLE users(
		pk INTEGER PRIMARY KEY AUTOINCREMENT,
		username VARCHAR(32),
		password VARCHAR(64)
	);'''
)

#Tweets table
cursor.execute(
	'''CREATE TABLE posts(
		pk INTEGER PRIMARY KEY AUTOINCREMENT,
		user_id INTEGER,
		time FLOAT,
		img VARCHAR,
		caption VARCHAR(140),
		FOREIGN KEY(user_id) REFERENCES users(pk)
	);'''
)