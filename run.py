import pyperclip
from passcord import User, Creadentials

def creat_user(name, passcord):
    '''creates a new user account'''
    new_user_user = User(name, passcord)
    return new_user_user


def save_user(user):
    '''saves the user's account'''
    User.save_user(user)

def verify_my_user(name, passcord):
    ver_user = Credentials.check_user(name,passcord)
	return ver_user

def generate_passcord():
    generat_pscord = Creadentials.generat_pscord()
    return generat_pscord

def create_credentials(account, name,passcord,site):
    '''creates a new credentials'''
    new_credentials = Credentials.(account, name,passcord,site)
    return new_credentials

def save_credentials(credential):
    '''saves the new credential'''
    Credentials.save_credentials(credential)

def disply_credentials(name):
    '''displays the credentials saved by the user'''
    return Credentials.disply_credentials(name)

def copy_credentials(site):
    '''copys credentials to the clipboard'''
    return Credentials.copy_credentials(site)
    
    