import string
from random import *
from passcord import User
from passcord import Credentials
def create_user(firstname,lastname,username,userpassword):
    newuser= User(firstname,lastname,username,userpassword)
    return newuser
def save_user(user):
    user.save_user()
def delete_user(user):
    user.delete_user()
def find_user(number):
    return User.find_by_number(number)
def display_users():
    return User.display_users()
def create_account(accountusername,accountname,accountpassword):
    newaccount= Credentials(accountusername,accountname,accountpassword)
    return newaccount
def save_account(user):
    user.save_account()
def delete_account(user):
    user.delete_account()
def find_account(number):
    return Credentials.find_by_number(number)
def display_accounts():
    return Credentials.display_accounts()
def main():
        while True:
            print("Welcome to Passcord  write ...choose the following to start RG for signing up or LG for logging up ")
            print("RG -or- LG")
            option=input()
            if option == "RG":
                print("Create Account")
                print("-"*10)
                print("Enter your First Name..")
                firstname=input()
                print("Enter your Last Name..")
                lastname=input()
                print("Please Set your username..")
                username=input()
                print("Set your password..")
                userpassword=input()
                save_user(create_user(firstname,lastname,username,userpassword))
                print("Your account was created successfully.These are u acc details:")
                print("-"*10)
                print(f"Name: {firstname} {lastname} \nUsername: {username} \nPassword: {userpassword}")
                print("\nUse Login to your account with your details")
                print("\n \n")
                # for user in display_users():
                #     print(f"{user.firstname} {user.lastname}.....{user.username}")
            elif option =="LG":
                print(" your Username..")
                loginUsername=input()
                print("your Password..")
                loginPassword=input()
                if find_user(loginPassword):
                    print("\n")
                    print("your can create multipe accounts (MAC) and also view them (MVC)")
                    print("-"*60)
                    print("MAC -or- MVC")
                    choose= input()
                    print("\n")
                    if choose == "MAC":
                        print("Add Your cred Account")
                        print("-"*25)
                        accountusername=loginUsername
                        print("Account Name")
                        accountname=input()
                        print("\n")
                        print("Generate automatic password(G) or Create new password(C)?")
                        decision=input()
                        if decision=="G":
                            characters=string.ascii_letters + string.digits
                            accountpassword="".join(choice(characters)for x in range(randint(6,16)))
                            print(f"Password: {accountpassword}")
                        elif decision=="C":
                            print("Enter your Password")
                            accountpassword=input()
                        else:
                            print("please put in a valid choice")
                        save_account(create_account(accountusername,accountname,accountpassword))
                        print("\n")
                        print(f"Username:{accountusername} \nAccount Name: {accountname} \nPassword: {accountpassword}")
                    elif choose == "VC":
                        if find_account(accountusername):
                            print("Here is a list of your created accounts: ")
                            print("-"*25)
                            for user in display_accounts():
                                print(f"Account: {user.accountname} \nPassword: {user.accountpassword} \n\n")
                        else:
                            print("Invalid creds!")
                    else:
                        print("PLEASE TRY AGAIN!")
                        print("\n")
                else:
                    print("Incorrect INFO please try again! Thankyou")
                    print("\n")
            else:
                print("Kindly choose a valid option")
                print("\n")
if __name__ == '__main__':
     main()