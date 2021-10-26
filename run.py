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

def main():
    print("Hello...and Welcome to password locker")

    while True:
        print("-"*60)
        print("use these short code to navigate through: \n ca - Create Account \n li - Log In \n ex - Exit")
        short_code = input("Enter a choice: ").lower().strip()

        if short_code == 'ex':
            break
        
        elif short_code == 'ca':
            print("-"*60)
            print('To ccreate new account: ')
            name = input("Enter user name - ").strip()
            passcord = input("Enter your passcord- ").strip
            save_user(creat_user(name, passcord))
            print(" ")


        elif short_code == 'li':
            print("-"*60)
            print("To log in enter your account details: ")
            name = input("fill your name - ")
            passcord = input("fill your your passcord - ")
            user_existence = verify_my_user(name,passcord)
            if user_existence == name:
                print(f'Welcome {name}. would you like to continue? ')
                while True:
                    print("-"*60)
                    print('Onother navigation short codes: \n cc-Create a Credential \n dc-Display Credentials \n copy-Copy Password \n ex-Exit')
                    short_code = input("fill your choice:").lower().strip()
                    print("-"*60)

                    if short_code == 'ex':
                        print(f'goodbye{name}')
                        break


                    elif
                    

    
