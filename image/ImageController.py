from flask import Flask,request, session, Blueprint
from .ImageService import ImageService
from user.UserService import UserService
import boto3

image_controller = Blueprint('image_controller', __name__)

imageService = ImageService.getInstance()
userService = UserService.getInstance()

@image_controller.route('/api/image/uploadProfilePicture', methods=['POST'])
def uploadProfilePicture():
    if request.method == 'POST':
        file = request.files['file']
        filename = imageService.uploadImageToS3(file)
        if filename:
            imageService.setImageToIndex(userService.getCurrentId(), 0, filename)

        return filename

@image_controller.route('/api/image/updatePictureArrayOrder', methods=['POST'])
def updatePictureArrayOrder():
    newIndex = request.get_json()['params']['index']
    filename = request.get_json()['params']['uri']
    print(newIndex, filename)
    imageService.setImageToIndex(userService.getCurrentId(), newIndex, filename)
    return "ye"

@image_controller.route('/api/image/uploadFileAndUpdatePictureArrayOrder', methods=['POST'])
def uploadFileAndUpdatePictureArrayOrder():
    if request.method == 'POST':
        file = request.files['file']
        index = int(request.form['index'])
    
        filename = imageService.uploadImageToS3(file)
        if filename : 
            imageService.setImageToIndex(userService.getCurrentId(), index, filename)

    return "Success"



# @image_controller.route('/api/image/pushToPictureArray', methods=['POST'])
# def pushToPictureArray():
#     file = request.files['file']
#     filename = imageService.uploadImageToS3(file)
#     imageService.pushImageToUser(userService.getCurrentId(), filename)
#     return filename
