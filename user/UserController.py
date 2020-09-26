from flask import Flask, render_template, url_for, request, session, redirect, Blueprint
import bcrypt
from config.MongoConnectionConfig import MongoConnectionConfig

user_controller = Blueprint('user_controller', __name__)

mongoConnection = MongoConnectionConfig()
mongo = mongoConnection.connect()

@user_controller.route('/api/test', methods=['POST', 'GET'])
def test():
    print(session['phone_number'])
    print("test")
    return "test2"

@user_controller.route('/api/login', methods=['POST'])
def login():
    print(session['phone_number'])
    users = mongo.db.users
    login_user = users.find_one({'phone_number': request.get_json()['params']['phone_number']})
 
    if login_user:
        if bcrypt.hashpw(request.get_json()['params']['password'].encode('utf-8'), login_user['password']) == login_user['password']:
            session['phone_number'] = request.get_json()['params']['phone_number']
            return "User is logged in"

    return 'Invalid phone_number or password'

@user_controller.route('/api/logout')
def logout():
    print("ran")
    session.clear()
    return "ok"

@user_controller.route('/api/register', methods=['POST', 'GET'])
def register():
    print(request.get_json()['params'])
    if request.method == 'POST':
        users = mongo.db.users
        existing_user = users.find_one({'phone_number' : request.get_json()['params']['phone_number']})

        if existing_user is None:
            hashpass = bcrypt.hashpw(request.get_json()['params']['password'].encode('utf-8'), bcrypt.gensalt())
            users.insert({
                'phone_number':request.get_json()['params']['phone_number'], 
                'password': hashpass})
            session['phone_number'] =  request.get_json()['params']['phone_number']
            # return redirect(url_for('index'))
            return "phone_number has been registered"

        return 'That phone_number already exists!'

    # return render_template('register.html')
    return "phone_number has beens registered"

