# A rough architecture plan
**Stack:** python/flask
**DB:** PostgreSQL


##### Entities (Models in MVC (?))
(& - reference to)

**User**
- permissions
- submissions &
- about
- credentials

**Problem**
- test set:
	a set of files with input data and corresponding output answers
- checker
	a program to evaluate a submission, be it a source code or simply an answer
- statement (translation mechanism?)
	a problem statement (html?)
- submissions &

**Submission**
- source / text
- run info
- user info &
- result


**Contest**
- problems &
- scoring:
	time penalty, scores ( - should be highly customizable)
- submissions &
	each submission has a tag describing a contest it belongs to (to easily combine different conest runs)
- run
	start and finish time in combination with specified (by tags) submissions


##### Modules:
- Tester
	A module which compiles, runs and evaluates a submission against tests checker
- Dispatcher
	A module which distributes submissions to different Testers, providing scalability
- DatabaseHelper
	For all stuff related to DB (is it needed though? SQLAlchemy might be enough)
- API 
	Responds on everything on :80
- View
	Everything for frontend rendering goes here


###### What views / logic in it should we have?
	
