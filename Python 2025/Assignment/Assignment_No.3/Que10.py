'''
10. Write a program to check if person is eligible to marry or not (male age >=21 and 
female age>=18) 
'''
gender = str(input(" enter your gender in f/m : "))


gen = gender.lower()
if(gen == 'f' ):
    age = int(input(" enter your age : "))
    if(age >= 18):
        print(f"Hey miss. are you now {age} , you are eligible to marry")
    else:
        print("your not eligible")
else:
    age = int(input(" enter your age : "))
    if(age >= 21):
        print(f" you are now {age} , you are eligible to marry")
    else:
        print("your not eligible")