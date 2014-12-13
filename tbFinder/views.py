import tbFinder.db as db
import json
from tbFinder import app
from flask import Flask, render_template, request

@app.route('/allCourses')
def allCourses():
    # should show a page with all the current courses
    # get all entries from DB, render them somehow
    all_courses = {'CIS': ['110', '120', '121'], 'STSC': ['001', '100']}
    return render_template('allcourses.html', all_courses=all_courses)


@app.route('/course/<dept>')
@app.route('/course/<dept>/<course_id>')
def course(dept, course_id=None):
	if (course_id==None):
		results = db.get_all_dept_links(dept)
		return render_template('dept_results.html', dept=dept,
								results=json.loads(results))
	else:	
		results = db.get_all_course_links(dept, course_id)
		return render_template('courseid_results.html', dept=dept,
								course_id=course_id, results=json.loads(results))


@app.route('/add')
def add():
	return render_template('add.html')


@app.route('/addLink', methods=['POST'])
def addLink():
	db.add_tb_info(request.form)
	return render_template('success.html')
