from flask import Blueprint, render_template, request, flash, redirect, url_for
from flask_login import current_user, login_user
from website import views, auth
#from .models import Users, ActivityLog
from . import db
from werkzeug.security import generate_password_hash, check_password_hash
import json
from sqlalchemy import update

auth = Blueprint('auth', __name__)

@auth.route('/' , methods=['GET','POST'])
def login():
    return render_template("login.html")

@auth.route('/register' , methods=['GET','POST'])
def register():
    return render_template("register.html")