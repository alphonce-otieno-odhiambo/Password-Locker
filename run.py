import pyperclip
from passcord import User, Creadentials

def creat_user(name, ppasscord):
    '''creates a new user account'''
    new_user_user = User(name, passcord)
    return new_user_user


def save_user(user):
    '''saves the user's account'''
    User.save_user(user)