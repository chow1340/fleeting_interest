from flask import Flask,request, session, Blueprint, jsonify
from user.UserService import UserService
from .MatchService import MatchService
from bson.json_util import dumps


match_controller = Blueprint('match_controller', __name__)


userService = UserService.getInstance()
matchService = MatchService.getInstance()

# TODO working ont his now
@match_controller.route('/api/match/getMatches')
def getMatches():
    currentId = userService.getCurrentId()
    if currentId:
        currentUser = userService.getCurrentUserProfile()
        matchList = currentUser['matchList']
        result = matchService.getMatchesByList(matchList)

        
    return dumps(result)