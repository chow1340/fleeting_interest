from flask import Flask, render_template, url_for, request, session, redirect, Blueprint


class UserService():

    __instance = None

    @staticmethod
    def getInstance():
        """ Static access method. """
        if UserService.__instance == None:
            UserService()
        return UserService.__instance

    def __init__(self):
      """ Virtually private constructor. """
      if UserService.__instance != None:
         raise Exception("This class is a singleton!")
      else:
         UserService.__instance = self    

         
    def getCurrentUser(self):
        return session['phone_number']

    def getCurrentId(self):
        return session['_id']
    