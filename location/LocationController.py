from flask import Flask,request, session, Blueprint
from user.UserService import UserService
from .LocationService import LocationService


location_controller = Blueprint('location_controller', __name__)


userService = UserService.getInstance()
locationService = LocationService.getInstance()

@location_controller.route('/api/location/updateLocation', methods=['POST'])
def updateLocation():
    locationService.updateLocation(request.get_json()['params']['location'], userService.getCurrentId())
    user = locationService.updateGeocode(request.get_json()['params']['geocode'], userService.getCurrentId())
    return user