from flask import Blueprint, redirect, url_for, request, jsonify, flash, abort, render_template
from app.utils.db_utils import DatabaseUtil
from flask import current_app as app

auth = Blueprint('auth', __name__)

@auth.route('/api/users/login', methods=['GET', 'POST'])
def login_post():
    if request.method == "POST":
        username = request.form["username"]
        password = request.form["password"]
        email = None  # Initialize email variable

        # Check if the username is an email address
        if "@" in username:
            email = username
            username = None  # Set username to None if it's an email address
        databaseobj = DatabaseUtil()
        databaseobj.connect()
        user = databaseobj.get_user(username=username, email=email)
        if user:
            user_id = user["user_id"]
            if databaseobj.check_hashpasswd(user_id, password):
                app.config["CURRENT_USER"] = user_id
                databaseobj.close()
                return redirect(url_for('main.upload_page'))
        databaseobj.close()
        error = "Invalid email/username or password"
        return render_template('login.html', error=error )
    # jsonify({"message": "invalid username/email or password!"}), 400



@auth.route('/api/users/logout')
def logout():
    pass
    return 

@auth.route('/api/users/register', methods=['GET', 'POST'])
def register_post():
    if request.method == "POST":
        try:

            database = DatabaseUtil()
            database.connect()
            first_name = request.form["first_name"]
            last_name = request.form["last_name"]
            email = request.form["email_address"]
            password = request.form["password"]
            username = request.form["username"]
            user = {
            "firstName": first_name,
            "lastName": last_name,
            "email": email,
            "password": password,
            "username": username
            }
            database.create_user(user)
            database.close()
            return redirect(url_for('main.login_page'))
            # return jsonify({"message": "registration successful!"}), 200
        except Exception as e:
            return redirect(url_for('main.register'))