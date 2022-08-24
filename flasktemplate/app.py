#importing Flask class from flask library
from flask import Flask,redirect,url_for,request,jsonify,abort,render_template
import requests
from flask_material import Material

app=Flask(__name__)
Material(app)

'''
@app.route("/user/<name>")
def user(name):
    msg=f"<h1>Hello {name}!</h1>"
    greet=f"<h1>How are you doing {name}?</h1>"
    return msg+greet
'''
@app.route("/user/<name>")
def user(name):
    return render_template("user.html",username=name,n=10) #n is included to add a multiplication table

@app.route("/material/<name>")
def material(name):
    return render_template("material.html",username=name,n=10) 

