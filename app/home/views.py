from flask import abort, render_template
from flask_login import current_user, login_required

from . import home

@home.route('/')
@home.route('/home')
def homepage():
    return render_template('home/home.html', title='Home Page')


