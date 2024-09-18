from flask import Blueprint, jsonify, request, render_template
from app.utils.db_utils import DatabaseUtil
from app.utils.image_utils import CompressImage

main = Blueprint('main', __name__)

@main.route('/')
@main.route('/index')
def index():
    return render_template('index.html')
@main.route('/login')
def login_page():
    return render_template('login.html')

@main.route('/download')
def download():
    return render_template('download.html')

@main.route('/register')
def register():
    return render_template('register.html')
@main.route('/profile')
def profile():
    return render_template('profile.html')
@main.route('/upload')
def upload_page():
    return render_template('upload.html')

