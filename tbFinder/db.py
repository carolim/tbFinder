from flask import *
import sqlite3

DATABASE = 'data.db'

# we need methods to:
# insert textbook information into db (posted by usr)
# fetch all textbooks corresponding to a particular dept
# fetch all textbooks corresponding to a particular dept AND course

def add_tb_info(form):
	conn = sqlite3.connect(DATABASE)
	c = conn.cursor()
	dept = form['dept']
	id = form['id']
	name = form['tb_name']
	link = form['tb_link']
	c.execute('insert into textbooks (dept, id, name, link) values (?, ?, ?, ?)', 
				(dept, id, name, link));
	conn.commit()
	conn.close()
	return "successfully added items"

