from flask import Flask
from flask import render_template;
app=Flask(__name__);
@app.route("/<username>")
def index(username):
	return render_template('Home.html',uname=username);

	
if __name__=="__main__":
	app.run("127.0.0.1",4444,debug=True)