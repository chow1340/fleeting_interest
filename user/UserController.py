from flask import Flask, render_template, url_for, request, session, redirect, Blueprint
import bcrypt
from config.MongoConnectionConfig import MongoConnectionConfig
from bson import json_util, ObjectId
from bson.json_util import dumps
import json
from datetime import datetime


user_controller = Blueprint('user_controller', __name__)

mongoConnection = MongoConnectionConfig.getInstance()
mongo = mongoConnection.connect()
users = mongo.db.users


@user_controller.route('/api/user/test', methods=['POST', 'GET'])
def test():
    print(session['phone_number'])
    print("test")
    return "test2"

@user_controller.route('/api/user/login', methods=['POST'])
def login():
    users = mongo.db.users
    login_user = users.find_one({'phone_number': request.get_json()['params']['phone_number']})
 
    if login_user:
        if bcrypt.hashpw(request.get_json()['params']['password'].encode('utf-8'), login_user['password']) == login_user['password']:
            session['phone_number'] = request.get_json()['params']['phone_number']
            # objectId = json_util.dumps(ObjectId(login_user['_id']), default=json_util.default)
            objectId = json.loads(json_util.dumps(login_user['_id']))
            session['_id'] = objectId['$oid']
            return "Login Successsful"

    return 'Invalid phone_number or password'

@user_controller.route('/api/user/logout')
def logout():
    session.clear()
    return "logout successful"

@user_controller.route('/api/user/register', methods=['POST', 'GET'])
def register():
    if request.method == 'POST':
        users = mongo.db.users
        existing_user = users.find_one({'phone_number' : request.get_json()['params']['phone_number']})

        if existing_user is None:
            hashpass = bcrypt.hashpw(request.get_json()['params']['password'].encode('utf-8'), bcrypt.gensalt())
            user = users.insert({
                'phone_number':request.get_json()['params']['phone_number'], 
                'password': hashpass,
                'date_created': datetime.now(),
                'first_name': "",
                'last_name' : "",
                })
            session['phone_number'] =  request.get_json()['params']['phone_number']
            session['_id'] = ObjectId(user['_id'])

            return "phone_number has been registered"

        return 'That phone_number already exists!'

    # return render_template('register.html')
    return "phone_number has beens registered"


@user_controller.route('/api/user/getCurrentUser', methods=['GET'])
def getCurrentUser():
    currentSessionNumber = session['phone_number']
    users = mongo.db.users
    currentUser = dumps(users.find_one({'phone_number' : currentSessionNumber}, {"password" : False}))
    return currentUser

# TODO add error handling
@user_controller.route('/api/user/editProfile', methods=['POST'])
def editProfile():
    users = mongo.db.users
    newValues = request.get_json()['params']['currentProfile']

    if newValues:
        user = dumps(users.find_one_and_update({'_id' : ObjectId(newValues['_id']['$oid'])}, {'$set': {'first_name' : newValues['first_name'], \
        'last_name' : newValues['last_name']}}, upsert=False))


    return user 
    

