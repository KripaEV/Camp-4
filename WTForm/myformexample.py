from flask import Flask, render_template
from myformclass import NameForm

app=Flask(__name__)

#include a secret key to prevent CSRF attack
app.config["SECRET_KEY"]="secret"

@app.route("/enquiry",methods=["GET","POST"])
def enquiry():
    form=NameForm() #creating an instance class from Flaskform
    name=None
    #checks if form was submitted and if all validators are passed, then only it is validated 
    if form.validate_on_submit(): 
        name=form.name.data
        form.name.data=' ' 
    return render_template('enquiry.html',form=form, name=name) #not sure about the syntax

#check if its the main module, then run the app
if __name__=="__main__":
    app.run(debug=True)
