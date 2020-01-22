from flask import Flask
app = Flask(__name__)

@app.route("/")
@app.route("/home")
def hello():
	return "<h>Hello Internet!</h>"

@app.route("/about")
def about():
	return "<h>About the page</h>"

if __name__=='__main__':
	app.run(debug=True)

