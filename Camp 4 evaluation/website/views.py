from tkinter.tix import ROW
from flask import Blueprint, render_template, request, jsonify, url_for, redirect, flash
from . import db
from .models import Users, BlogPosts, Comments
import json
from sqlalchemy import func, Date, desc
from datetime import date
from flask_login import login_user, login_required, logout_user, current_user
from functools import wraps

views = Blueprint('views', __name__)

blogs=[]

@views.route('/home', methods=['GET', 'POST'])
def dashboard():
    if request.method == "POST":
        blogId=request.form.get('blogId')
        blogTitle=request.form.get('blogTitle')
        blogDescSmall=request.form.get('descSmall')
        blogDescBig=request.form.get('descBig')
        print(blogId,blogTitle,blogDescSmall,blogDescBig)
        post=BlogPosts(blogId=blogId,blogTitle=blogTitle,blogDescSmall=blogDescSmall,blogDescBig=blogDescBig)
        db.session.add(post)
        db.session.commit()
    
    #blogs=BlogPosts.query.order_by(BlogPosts.blogId)
    return render_template('home.html',blogs=blogs, listAll=True)

@views.route('/readmore', methods=['GET', 'POST'])
def details():
    return render_template('readMore.html')