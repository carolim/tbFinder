from flask import *
import sqlite3
import json

DATABASE = 'data.db'

# custom decorators for sorting & debugging
def debug(f):
	def new_f(*args):
		result = f(*args)
		print "result of method call: " + str(result)
		return result
	return new_f


# adds a textbook to the db
@debug
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
	return name + " successfully added to the textbooks database!"


# returns a sorted dictionary in the form {'deptname': [list of course codes]}
@debug
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
@debug
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
@debug
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


@debug
def search(query):
	conn = sqlite3.connect(DATABASE)
	c = conn.cursor()

	cursor = c.execute('''
		select * from textbooks where code like ?''',
		(int(query),))
	results = cursor.fetchall()
	conn.close()
	
	l = []
	for result in results:
		l.append(dict(dept=result[1], code=result[2],
					name=result[3], link=result[4]))
	return l


