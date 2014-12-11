from tbFinder import app

@app.route('/')
def index():
    return 'first route yeahhhhhhhhh'

@app.route('/allCourses')
def allCourses():
    #should show a page with all the current courses
    return courses!