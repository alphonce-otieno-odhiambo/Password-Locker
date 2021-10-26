#!/usr/bin/env python3.9
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
    ver_user = Creadentials.check_user(name,passcord)
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


                    elif short_code == 'cc':
                        print("-"*60)
                        print("Enter your credential details: ")
                        site = input("enter your site name ").strip()
                        account = input("Enter your account name: ").strip()
                        while True:
                            print("-"*60)
                            print('Please choose an option for entering a password: \n ep-enter existing password \n gp-generate a password \n ex-exit')
							psw_choice = input('Enter an option: ').lower().strip()
							print("-"*60)
                            if psw_choice =='ep':
                                passcord = input("enter your psscord: ").strip(
                                break
                            elif psw_choice == 'gp':
                                passcord = generate_passcord()
                                break
                            elif psw_choice == 'ex':
                                break
                            else:
                                print("oow!! Wrong option entered. Please try again")
                        save_credentials(create_credentials(account, name, passcord, site))
                        print(f'Credentials Created: site{site} - Account Name:{account} - Passcord:{passcord} ')
                    elif short_code == 'dc':
                        if disply_credentials(name):
                            print("Here is the list of your credentials ")
                            for credentia in disply_credentials(name):
                                print(f'Site Name:{credentia.site}- Account Name {credentia.account}- Passcord {credentia.passcord} ')
                        else:
                            print("you don't seem to have any credentials yet! ")
                    elif short_code = 'copy':
                        site_choosen = input('Enter the site name for the credential passcord to copy: ')
                        copy_credentials(site_choosen)
                    else:
                        print("wooow! Wring option entered ")

            else:
                print("Wrong option, try gain or create a new account")
        else:
            print("-"*60)
            print("Wrong option entered, please try again. ")



if __name__ =='__main__':
    main()



                        

                    

    
