from flask import *
import sqlite3
import json

DATABASE = 'data.db'

# we need methods to:
# delete tb info
# fetch all textbooks corresponding to a particular dept
# fetch all textbooks corresponding to a particular dept AND course
def add_tb_info(form):
	conn = sqlite3.connect(DATABASE)
	c = conn.cursor()
	dept = form['dept']
	code = int(form['id'])
	name = form['tb_name']
	link = form['tb_link']
	c.execute('insert into textbooks (dept, code, name, link) values (?, ?, ?, ?)', 
				(dept, code, name, link));
	conn.commit()
	conn.close()


def get_all_dept_links(dept):
	conn = sqlite3.connect(DATABASE)
	c = conn.cursor()
	cursor = c.execute('''
		select * from textbooks where dept = ? order by code''',
		(dept,))
	results = cursor.fetchall()
	conn.close()
	print json.dumps({"results": results})
	return json.dumps(results)


# returns results for a particular course within a dept
def get_all_course_links(dept, course_id):
	conn = sqlite3.connect(DATABASE)
	c = conn.cursor()
	cursor = c.execute('''
		select * from textbooks where (dept = ? and code = ?)''',
		(dept, course_id))
	results = cursor.fetchall()
	conn.close()
	return json.dumps(results)


