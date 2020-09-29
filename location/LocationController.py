from flask import Flask, render_template, url_for, request, session, redirect, Blueprint
from user.UserService import UserService
from .LocationService import LocationService


location_controller = Blueprint('location_controller', __name__)


userService = UserService.getInstance()
locationService = LocationService.getInstance()

@location_controller.route('/api/location/updateLocation', methods=['POST'])
def updateLocation():
    print("ran")
    currentUser = userService.getCurrentUser()
    locationService.updateLocation(request.get_json()['params']['location'], userService.getCurrentId())
    return "xd"