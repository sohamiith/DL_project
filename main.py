from flask import Flask, jsonify, request, render_template
from fun import *
app = Flask(__name__)

@app.route("/")
def index():
    return render_template('index.html')

@app.route("/sum/<int:a>/<int:b>")
def sum(a,b):
	ans = str(sum1(a,b))
	result = {
		"a" : a,
		"b" : b,
		"operation": "+",
		"ans": ans
	}
	return jsonify(result)

@app.route("/min/<int:a>/<int:b>")
def min(a,b):
	ans = str(min1(a,b))
	result = {
		"a" : a,
		"b" : b,
		"operation": "-",
		"ans": ans
	}
	return jsonify(result)

@app.route("/div/<int:a>/<int:b>")
def div(a,b):
	ans = str(div1(a,b))
	result = {
		"a" : a,
		"b" : b,
		"operation": "/",
		"ans": ans
	}
	return jsonify(result)

@app.route("/mul/<int:a>/<int:b>")
def mul(a,b):
	ans = str(mul1(a,b))
	result = {
		"a" : a,
		"b" : b,
		"operation": "*",
		"ans": ans
	}
	return jsonify(result)

if __name__=="__main__":
	app.run(debug=True)