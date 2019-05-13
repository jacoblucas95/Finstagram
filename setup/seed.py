#!/usr/bin/env python3

import sqlite3

connection = sqlite3.connect('insta.db', check_same_thread=False)
cursor=connection.cursor()

cursor.execute('''INSERT INTO users(
					username,password)
					VALUES(?,?);''',(
					'kylie','kanye')
				)

cursor.execute('''INSERT INTO posts(
					user_id,time,post)
					VALUES(?,?,?);''',(
					'1',1556548203,'https://nyppagesix.files.wordpress.com/2019/02/spl5066306_009-1.jpg?quality=90&strip=all&w=618&h=410&crop=1')
				)
