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

@image_controller.route('/api/image/deleteImage', methods=['POST'])
def deleteImage():
    if request.method == 'POST':
        fileKey = request.get_json()['fileKey']
        imageService.deleteImageFromS3(fileKey)
        imageService.deleteImageFromUserByPicture(userService.getCurrentId(), fileKey)
        return "Image has been deleted"


@image_controller.route('/api/image/updatePictureArrayOrder', methods=['POST'])
def updatePictureArrayOrder():
    newIndex = request.get_json()['index']
    filename = request.get_json()['uri']
    imageService.setImageToIndex(userService.getCurrentId(), newIndex, filename)
    return "Picture array order updated"

@image_controller.route('/api/image/uploadFileAndUpdatePictureArrayOrder', methods=['POST'])
def uploadFileAndUpdatePictureArrayOrder():
    if request.method == 'POST':
        file = request.files['file']
        index = int(request.form['index'])
    
        filename = imageService.uploadImageToS3(file)
        if filename : 
            imageService.setImageToIndex(userService.getCurrentId(), index, filename)

    return filename



