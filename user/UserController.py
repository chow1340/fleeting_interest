from flask import Flask, render_template, url_for, request, session, redirect, Blueprint
import bcrypt
from config.MongoConnectionConfig import MongoConnectionConfig

user_controller = Blueprint('user_controller', __name__)

mongoConnection = MongoConnectionConfig()
mongo = mongoConnection.connect()

@user_controller.route('/test', methods=['POST'])
def test():
    print("test")
    return "test"

@user_controller.route('/login', methods=['POST'])
def login():
    users = mongo.db.users
    login_user = users.find_one({'name': request.values['username']})
 
    if login_user:
        if bcrypt.hashpw(request.values['password'].encode('utf-8'), login_user['password']) == login_user['password']:
            session['username'] = request.values['username']
            return redirect(url_for('index'))

    return 'Invalid username or password'

@user_controller.route('/logout')
def logout():
    print("ran")
    session.clear()
    return "ok"

@user_controller.route('/register', methods=['POST', 'GET'])
def register():
    if request.method == 'POST':
        users = mongo.db.users
        existing_user = users.find_one({'name' : request.values['username']})

        if existing_user is None:
            hashpass = bcrypt.hashpw(request.values['password'].encode('utf-8'), bcrypt.gensalt())
            users.insert({'name':request.values['username'], 'password': hashpass})
            session['username'] =  request.values['username']
            return redirect(url_for('index'))

        return 'That username already exists!'

    return render_template('register.html')

