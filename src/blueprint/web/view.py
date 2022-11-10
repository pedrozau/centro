from flask import render_template 


def index():
    return render_template('login-dark-login.html')

def login():
    return render_template('login-light-login.html')