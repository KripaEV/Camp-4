from flask import Flask

app=Flask(__name__)

#include a secret key to prevent CSRF attack
app.config["SECRET_KEY"]="secret"

