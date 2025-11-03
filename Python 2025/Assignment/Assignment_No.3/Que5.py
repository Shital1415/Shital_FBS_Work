'''
5. Write a program to check whether the triangle is equilateral, isosceles or scalene 
triangle. 
'''
angle1 = int(input("Enter the 1st angle of triangle :"))
angle2 = int(input("Enter the 2nd angle of triangle :"))
angle3 = int(input("Enter the 3rd angle of triangle :"))
triangle = angle1 + angle2 + angle3 
if(triangle == 180 and angle1 > 0 and angle2 >0 and angle3 > 0):
    if( angle1 == 60 and angle2 == 60 and angle3 == 60):
        print("given traingle is equilateral")
    elif( angle1==angle2 or angle2==angle3 or angle3 == angle1):
        print("given traingle is isosceles")
    else:
        print("given traingle is scalene")
else:
    print(f"the given angles {angle1} ,{angle2} , {angle3} are invalid")