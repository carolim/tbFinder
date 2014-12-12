from tbFinder import app
from flask import Flask, render_template

@app.route('/')
def index():
    return 'first route yeahhhhhhhhh'

@app.route('/allCourses')
def allCourses():
    #should show a page with all the current courses
    #get all entries from DB, render them somehow
    all_courses = {'CIS': ['110', '120', '121'], 'STSC': ['001', '100']}
    return render_template('allcourses.html',
    						all_courses=all_courses)