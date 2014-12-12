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
		# only dept specified
		# call to method to fetch all courses from db, e.g from STSC
		return "No course id!"
	else:	
		# call to method to fetch particular course from db, i.e STSC 001
		return "Params: %s" % dept

@app.route('/add')
def add():
	return render_template('add.html')

#TODO: should be post only
@app.route('/addLink')
def addLink():
	# route to add link information to the db
	return "todo"
