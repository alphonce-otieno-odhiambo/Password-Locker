import random
import pyperclip
import string
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

    @classmethod
    def display_user(cls):
        return cls.user_list_in
    '''class method that returns the user details'''

    def delete_user(self):
        User.user_list_in.remove(self)

class Creadentials:

    ''' class for account creation, generation of passcords and saving infors'''
    creadentials_list_in = []


    @classmethod
    def checkin_user(cls):
        '''method that checks if the details entered are similar to the one in user_list_in'''

        user_currently = ''

        for useruser in User.user_list_in:
            if(useruser.name == name and useruser.passcord == passcord):
                user_currently = useruser.name

                return user_currently
    def __innit__(self,account, name, passcord):
        '''A method with instances for user's credentials'''
        self.account = account
        self.name = name
        self.passcord = passcord

    def save_credentials(self):
        '''saves the credentials class oject details'''

        Creadentials.creadentials_list_in.append(self)

    
    def generate_new_passcord(chara_size=12, charact=string.ascii_uppercase+string.ascii_lowercase+string.digits):
        '''funtion method that generates a 12 character passcord'''
        generate_passcord = ''.join(random.choice(charact) for in range(chara_size))
        return generate_passcord
    
    
    @classmethod
    def displying_credentials(cls, name):
        user_credential_list_in = []
        for credentia in cls.creadentials_list_in:
            if credentia.name == name:
                user_credential_list_in.append(credentia)
                return user_credential_list_in



    


    
    
        


