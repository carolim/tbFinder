from flask import *
import sqlite3
import json

DATABASE = 'data.db'


# adds a textbook to the db
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


# returns a dictionary in the form {'deptname': [list of course codes]}
def get_all_course_codes():
	conn = sqlite3.connect(DATABASE)
	c = conn.cursor()
	cursor = c.execute('''select * from textbooks''')
	results = cursor.fetchall()
	conn.close()
	
	d = {}

	for result in results:
		dept = result[1].strip()
		course_code = result[2]
		if dept not in d:
			d[dept] = [course_code]
		else:
			if course_code not in d[dept]:
				d[dept].append(course_code)
	return d


# returns results for a particular dept
def get_all_dept_links(dept):
	conn = sqlite3.connect(DATABASE)
	c = conn.cursor()
	cursor = c.execute('''
		select * from textbooks where dept = ? order by code''',
		(dept,))
	results = cursor.fetchall()
	conn.close()

	d = {}

	for result in results:
		course_code = result[2]
		if course_code not in d:
			d[course_code] = [dict(name=result[3], link=result[4])]
		else:
			d[course_code].append(dict(name=result[3], link=result[4]))

	return d


# returns results for a particular course within a particular dept
def get_all_course_links(dept, course_id):
	conn = sqlite3.connect(DATABASE)
	c = conn.cursor()
	cursor = c.execute('''
		select * from textbooks where (dept = ? and code = ?)''',
		(dept, course_id))
	results = cursor.fetchall()
	conn.close()

	l = []

	for result in results:
		l.append(dict(dept=result[1], code=result[2],
					 	name=result[3], link=result[4]))
	return json.dumps(l)

#TODO: need to fix this
def remove_from_db(link):
	conn = sqlite3.connect(DATABASE)
	c = conn.cursor()
	c.execute('''delete from textbooks where link=?''', (link,))
	conn.close()


