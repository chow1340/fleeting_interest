from flask import Flask, render_template, url_for, request, session, redirect
from user.UserController import user_controller
from location.LocationController import location_controller
from image.ImageController import image_controller
from datetime import timedelta


app = Flask(__name__)
app.register_blueprint(user_controller)
app.register_blueprint(location_controller)
app.register_blueprint(image_controller)

# timeout sessions
app.permanent_session_lifetime = timedelta(minutes=1440)

# TODO fix this secret key 
app.secret_key = "xd"


if __name__ == '__main__':
    # TODO change this key
    app.secret_key = 'mysecret'
    app.run(debug=True, host='192.168.2.40')