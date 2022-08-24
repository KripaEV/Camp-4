#importing Flask class from flask library
from flask import Flask,redirect,url_for,request,jsonify,abort
import requests

#create application instance with dunder
app=Flask(__name__) #contains name of main module

#defining a route in flask using app.route decorator
@app.route("/") #/ is root of website(default)
def greet(): #greet func is executed when accessing default route
    return "Have a good day!"

#can access this route by typing this arg into the url of the website
@app.route("/hello") #through this decorator it will execute the below function
def hello():
    return "<h1>Hello World!!</h1>"
'''
@app.route("/user/<name>") #accepts a name and displays it
def user(name):
    return f"<h2> hi {name} hello world!!</h2>"
'''
#demonstrating dynamic url building
@app.route("/admin")
def welcome_admin():
    return "Welcome admin"

@app.route("/guest/<guest>")
def hello_guest(guest):
    return f"<h2>Hello {guest}. You are our guest</h2>"

#one function to print stmts depending on name entered
@app.route("/user/<name>")
def hello_user(name):
    if name=="admin":
        return redirect(url_for("welcome_admin"))
    else:
        return redirect(url_for("hello_guest",guest=name))

#creating mylogin route for mylogin.html file
#demonstrating POST method which uses request obj
@app.route("/mylogin",methods=["POST"])
def mylogin():
    username=request.form["username"] #var in bracket is the name value in html
    password=request.form["password"]
    if username=="kripa" and password=="kripapass":#just random query not important
        return "Welcome %s" %username
    else: 
        return "username or password is not valid"
'''
#GET method frm above, change method in html as "get" (line 3)
@app.route("/mylogin",methods=["GET"])
def mylogin():
    username=request.args.get("username") #var in bracket is the name value in html
    password=request.args.get("password")
    if username=="kripa" and password=="kripapass":#just random query not important
        return "Welcome %s" %username
    else: 
        return "username or password is not valid"
'''
#or for the above 2 methods, create 2 urls with post and get so that only the url can be modified


#REST API methods
#create list of dictionaries
books=[{"id":1,"title":"Harry Potter", "author":"J.K. Rowling"},
        {"id":2,"title":"Jungle Book", "author":"Rudyard Kipling"},
        {"id":3,"title":"Alice in Wonderland", "author":"Lewis Caroll"}
      ]

#GET request to get data in json format
@app.route("/books", methods=["GET"])
def get_books():
    return jsonify({"books":books}) #jsonify converts list or dict to json format

#GET request to get particular book data using book id no in json format
@app.route("/books/<int:book_id>", methods=["GET"]) #typecasting 
def get_book(book_id):
    book =[book for book in books if book['id']==book_id]#list comprehension
    if len(book)==0:
        abort(404) #page not found
    return jsonify({"books":book[0]})

#POST request to save data into list 
@app.route("/books", methods=["POST"])
def create_book():
    #checks if received string is valid json
    if not request.json:
        abort(400) #bad request
    #create a new book as an dict item to be inserted 
    book={"id":books[-1]["id"]+1, 
    "title":request.json["title"],
    "author":request.json["author"]} #gets the id of the last item in list and adds one more value for the next item
    #append new item into books list
    books.append(book)
    return jsonify({"books":books}) 

#PUT request to edit data
@app.route("/books/<int:book_id>", methods=["PUT"]) #typecasting 
def update_book(book_id):
    book =[book for book in books if book['id']==book_id]#list comprehension
    if len(book)==0:
        abort(404) #page not found
    #check if json frm client has valid details
    if "title" in request.json and type(request.json["title"])!=str:
        abort(400) 
    if "author" in request.json and type(request.json["author"])!=str:
        abort(400) 
    book[0]["title"]=request.json["title"]
    book[0]["author"]=request.json["author"]

    return jsonify({"books":book[0]})

#delete request to remove data
@app.route("/books/<int:book_id>", methods=["DELETE"]) #typecasting 
def delete_book(book_id):
    book =[book for book in books if book['id']==book_id]#list comprehension
    if len(book)==0:
        abort(404) #page not found
    #remove item frm book list
    books.remove(book[0])
    return jsonify({"status":"deleted"})

#installing module called requests to send the API request
API_URL="https://api.genderize.io/?name={}" #defining the API url

#create a function to send api request to url
def send_api(name):
    print(API_URL)
    #sending api request using request.get() method
    try:
        data=requests.get(API_URL.format(name)).json()
    except Exception as exec:
        print(exec)
        data= None
    return data

#if we use browser default http method is GET4
@app.route("/gender/<name>")
def gender(name):
    response=send_api(name) #call the send_spi method, pass name and receive response
    return_text="Your name "+response["name"]+" is "+response["gender"]
    return return_text 

#check if its the main module, then run the app
if __name__=="__main__":
    app.run(host="0.0.0.0",debug=True)