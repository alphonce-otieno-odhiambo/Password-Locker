import random
import pyperclip
'''import the modules '''
class User:
    
    '''user class for creating class instances'''
    user_list_in = []
    '''user list for storing User objects'''

    '''create an instance of class'''
    def __innit__(self,name, passcord ):
        self.name = name
        self.passcord = passcord

