from flask import Flask, render_template,request, flash, redirect, url_for
from flask_sqlalchemy import SQLAlchemy

app=Flask(__name__)

#declaring database uri as key into flask config
#mssql+pyodbc://server/dbname?driver=driver
app.config["SQLALCHEMY_DATABASE_URI"]="mssql+pyodbc://DESKTOP-9FVJH8C\SQLEXPRESS/empdb?driver=driver"

#track modification key to false to optimize memory
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"]=False

#set secret key for forms
app.config["SECRET_KEY"]="secret"

#instantiate db obj
db=SQLAlchemy(app)

#create a class for model. class name is table name
class Employees(db.Model):
    id=db.Column("employee_id",db.Integer, primary_key=True)
    name=db.Column(db.String(100))
    salary=db.Column(db.Float(50))
    age=db.Column(db.String(50))

    #define constructor
    def __init__(self,name,salary,age):
        self.name=name
        self.salary=salary
        self.age=age

#route to list employees
@app.route("/")
def list_employees():
    return render_template("list.html",Employees=Employees.query.all())
#query.all shows all the data included

#route to add new employees
@app.route("/add",methods=["GET","POST"])
def addEmployee():
    #check if form was submitted by post method
    if request.method=="POST":
        if not request.form["name"] or not request.form["salary"] or not request.form["age"]:
            flash("please enter all the fields","error")
            return redirect(url_for("addEmployee"))
        else:
            #if all the var are set, proceed to add data
            employee=Employees(request.form["name"], request.form["salary"], request.form("age")) #craeting instance of obj
            #add and commit row of data
            db.session.add(employee)
            db.session.commit()
            flash("Record added successfully")
            return redirect(url_for("list_employees"))
    return render_template("add.html")
#query.all shows all the data included

if __name__=="__main__":
    db.create_all()
    app.run(debug=True)
