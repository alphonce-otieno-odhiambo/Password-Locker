import random
import pyperclip
'''import the modules '''
class User:
    
    '''user class for creating class instances'''
    user_list_in = []
    '''user list for storing User objects'''

    
    def __innit__(self,name, passcord ):
        '''create an instance of class'''
        self.name = name
        self.passcord = passcord
        
    
    def save_user(self):
    '''create a methord for saving the object'''
        User.user_list_in.append(self)

