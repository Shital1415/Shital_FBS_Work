'''
7. Write a program to check if user has entered correct userid and password. 
'''
user = 'shital'
password = 'Shital@123'

user_id = str(input("enter your user id :"))
passw = str(input("enter your password :"))

if(user_id == user and passw == password):
    print("user login successfully...")
else:
    print("user crendentials are invalid")