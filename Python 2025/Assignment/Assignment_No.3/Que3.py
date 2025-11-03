'''
3. Write a program to input angles of a triangle and check whether triangle is valid or not. 
'''
angle1 = int(input("Enter the 1st angle of triangle :"))
angle2 = int(input("Enter the 2nd angle of triangle :"))
angle3 = int(input("Enter the 3rd angle of triangle :"))

triangle = angle1 + angle2 + angle3 

## here we need to check the  """ angle > 0 ""
if(triangle == 180 and angle1 > 0 and angle2 >0 and angle3 > 0):
    print("the traingle is valid" )
else:
    print("the traingle is invalid" )