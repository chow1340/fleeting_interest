from flask import Flask,request, session, Blueprint
from user.UserService import UserService
from .ChatService import ChatService
from bson.json_util import dumps
from datetime import datetime

chat_controller = Blueprint('chat_controller', __name__)


userService = UserService.getInstance()
chatService = ChatService.getInstance()

@chat_controller.route('/api/chat/updateChatStatus', methods=['POST'])
def updateChatStatus():
    chatService.updateLastMessage(request.get_json()['params']['chatId'], request.get_json()['params']['message'])
    chatService.updateTotalMessages(request.get_json()['params']['chatId'])
    chatService.updateLastMessageDate(request.get_json()['params']['chatId'], datetime.now())

    return "Updated Chat Status"

@chat_controller.route('/api/chat/getChat', methods=['GET'])
def getChat():
    chatStatus = chatService.getChat(request.args.get("chatId"))
    return dumps(chatStatus)

# @chat_controller.route('/api/chat/setIsRead')
# def setIsRead():
#     chatService.setIsRead(request.get_json()['params']['isRead'])