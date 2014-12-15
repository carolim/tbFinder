import tbFinder.db as db
import json
from tbFinder import app
from flask import Flask, render_template, redirect, request

@app.route('/allCourses')
def allCourses():
    all_courses = db.get_all_course_codes()
    return render_template('allcourses.html', all_courses=all_courses)


@app.route('/course/<dept>')
@app.route('/course/<dept>/<course_id>')
def course(dept, course_id=None):
	if (course_id==None):
		results = db.get_all_dept_links(dept)
		return render_template('dept_results.html', dept=dept,
								results=results)
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
	return redirect('/allCourses')


@app.errorhandler(404)
def page_not_found(e):
	return render_template('404.html'), 404
