tbFinder
========
what needs to be done:

1. ROUTES
(GET/POST):
/home (where users can enter their email, before they can use the site)
/allCourses (main page users see after they are validated, lists all the current courses that have links posted)
/add (page where you can post textbook link)
/course?name=CIS110 (page where links for a particular course are listed)


(POST ONLY):
/validate (validates that the email entered is a Penn email)
/postLink (actually adding textbook to db)
/search (search for particular course (add search for textbooks as well?))

2. VIEWS
(add stuff here)

3. DATABASES
textbooks
[DEPARTMENT(e.g CIS), courseID(e.g 110), link to tb(e.g http://example.com/cis110tb)]
