'''
8. Write a program to prompt user to enter userid and password. After verifying 
userid and password display a 4 digit random number and ask user to enter the 
same. If user enters the same number then show him success message otherwise 
failed. (Something like captcha) 
'''
import random
user = 'shital'
password = 'Shital@123'

user_id = str(input("enter your user id :"))
passw = str(input("enter your password :"))

#i=1
if(user_id == user and passw == password):
    #for i in range(1, i+1):
    captcha = random.randint(0,9)+1234
    print("New captcha : " , captcha)
    cap = int(input("enter correctly captcha :"))
    if( captcha == cap):
        print("user login successfully...")
    else:
        print(" Re-enter the Captcha")
else:
    print("user crendentials are invalid")

    


