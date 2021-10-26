import unittest
import pyperclip
from passcord.py import User, Creadentials

class TestUser(unittest.TestCase):
	'''
	Test class that defines test cases for the user class behaviours.
	Args:
	    unittest.TestCase: helps in creating test cases
	'''
	def setUp(self):
		'''
		Function to create a user account before each test
		'''
		self.new_user = User('Ali','ali101')

	def test__init__(self):
		'''
		Test to if check the initialization/creation of user instances is properly done
		'''
		self.assertEqual(self.new_user.name,'Ali')
		
		self.assertEqual(self.new_user.passcord,'ali101')

	def test_save_user(self):
		'''
		Test to check if the new users info is saved into the users list
		'''
		self.new_user.save_user()
		self.assertEqual(len(User.user_list_in),1)

class TestCredentials(unittest.TestCase):
	'''
	Test class that defines test cases for the credentials class behaviours.
	Args:
	    unittest.TestCase: helps in creating test cases
	'''
	def test_check_user(self):
		'''
		Function to test whether the login in function check_user works as expected
		'''
		self.new_user = User('Ali','ali101')
		self.new_user.save_user()
		user2 = User('kodak','ali101')
		user2.save_user()

		for user in User.user_list_in:
			if user.name == user2.name and user.password == user2.password:
				current_user = user.name
		return current_user

		self.assertEqual(current_user,Creadential.check_user(user2.password,user2.name))

	def setUp(self):
		'''
		Function to create an account's credentials before each test
		'''
		self.new_credential = Creadentials('Ali','Facebook','kodakali','ali101')

	def test__init__(self):
		'''
		Test to if check the initialization/creation of credential instances is properly done
		'''
		self.assertEqual(self.new_credential.user_name,'Ali')
		self.assertEqual(self.new_credential.site_name,'Facebook')
		self.assertEqual(self.new_credential.account_name,'kodakali')
		self.assertEqual(self.new_credential.password,'ali101')

	def test_save_credentials(self):
		'''
		Test to check if the new credential info is saved into the credentials list
		'''
		self.new_credential.save_credentials()
		twitter = Creadential('Ozzz','Twitter','oozbryo','pswd100')
		twitter.save_credentials()
		self.assertEqual(len(Creadential.credentials_list),2)

	# def test_generate_password(self):
	# 	'''
	# 	Test to check if the generate password generates 8 character long alphanumeric numbers
	# 	'''
	# 	self.twitter = Credential('Twitter','maryjoe','')
	# 	self.twitter.password = generate_password()
	# 	self.assertEqual()

	def tearDown(self):
		'''
		Function to clear the credentials list after every test
		'''
		Credential.creadentials_list_in = []
		User.user_credential_list_in = []

	def test_display_credentials(self):
		'''
		Test to check if the display_credentials method, displays the correct credentials.
		'''
		self.new_credential.save_credentials()
		twitter = Credentials('Ali','Twitter','kodakali','ali101')
		twitter.save_credentials()
		gmail = Credentials('Ali','Gmail','kodakali','ali200')
		gmail.save_credentials()
		self.assertEqual(len(Creadentials.display_credentials(twitter.user_name)),2)

	def test_find_by_site_name(self):
		'''
		Test to check if the find_by_site_name method returns the correct credential
		'''
		self.new_credential.save_credentials()
		twitter = Credential('Ali','Twitter','kodakali','ali100')
		twitter.save_credentials()
		credential_exists = Creadentials.find_by_site('Twitter')
		self.assertEqual(credential_exists,twitter)

	def test_copy_credential(self):
		'''
		Test to check if the copy a credential method copies the correct credential
		'''
		self.new_credential.save_credentials()
		twitter = Creadentials('Ali','Twitter','kodakali','ali101')
		twitter.save_credentials()
		find_credential = None
		for credential in Creadentials.user_credentials_list:
				find_credential =Creadentials.find_by_site_name(credential.site_name)
				return pyperclip.copy(find_credential.password)
		Creadentials.copy_credential(self.new_credential.site_name)
		self.assertEqual('ali101',pyperclip.paste())
		print(pyperclip.paste())

if __name__ == '__main__':
	unittest.main(verbosity=2)