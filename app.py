from flask import Flask, render_template,request, make_response,session,redirect
from functools import wraps

app = Flask(__name__)
app.secret_key = 'super secret key'

# Define priviledge of API
config = {"read":"READ","write":"WRITE","delete":"DEL"}

# Wrapper function for blocking unauthorized access
def access(f):
	@wraps(f)
	def wrap(*args, **kwargs):
		p = session.get("privilege",[])
		functionPriviledge = config.get(f.__name__,[])
		if functionPriviledge not in p:
			return "Access denied"
		return f(*args, **kwargs)
	return wrap

# Wrapper function for blocking unauthorized access
def logged_in(f):
	@wraps(f)
	def wrap(*args, **kwargs):
		if session.get("logged_in","") != "true":
			return "Access denied"
		return f(*args, **kwargs)
	return wrap

# Class to return user priviledge
class userprivilege:
	def __init__(self,user):
		self.user = user

	def privilege(self):
		if self.user == "admin":
			return ["READ","WRITE","DEL"]
		elif self.user == "user1":
			return ["READ"]
		elif self.user == "user2":
			return ["WRITE"]
		elif self.user == "user3":
			return ["DEL"]

@app.route("/",methods=['GET'])
def index():
	return render_template("/login.html")


@app.route("/display",methods=['GET'])
@logged_in
def display():
	return render_template("/display.html")

@app.route("/logout",methods=['GET'])
def logout():
	session["logged_in"] = ""
	session["privilege"] = []
	return redirect("/")

@app.route("/loginB",methods=['POST'])
def login():
	userid = request.form.get("user_name","")
	password = request.form.get("password","")
	useridToStore = ""
	if userid == "admin" and password == "admin":
		useridToStore = userid

	if userid == "user1" and password == "user1":
		useridToStore = userid
	if userid == "user2" and password == "user2":
		useridToStore = userid
	if userid == "user3" and password == "user3":
		useridToStore = userid
	
	if len(useridToStore) != 0:
		p = userprivilege(useridToStore)
		privilege = p.privilege()
		print (privilege)
		session["privilege"] = privilege
		session["logged_in"] = "true"
		session["userid"] = userid
		return redirect("/display")
	else:
		return "Invalid credential"

@app.route("/read",methods=['GET'])
@access
def read():
	return "Operation of read"

@app.route("/write",methods=['GET'])
@access
def write():
	return "Operation of write"

@app.route("/del",methods=['GET'])
@access
def delete():
	return "Operation of delete"


if __name__ == "__main__":
    app.run(host='0.0.0.0',port=8090,debug=True)
	
