from flask import Flask,request, session, Blueprint
from user.UserService import UserService
from .ChatService import ChatService
chat_controller = Blueprint('chat_controller', __name__)


userService = UserService.getInstance()
chatService = ChatService.getInstance()

@chat_controller.route('/api/chat/setChatId', methods=['POST'])
def setChatId():
    chatId = request.get_json()['params']['chatId']
    chatService.setChatId(chatId)
    return chatId