'''
9. Input 5 subject marks from user and display grade(eg.First class,Second class ..) 
'''
sub1 = int(input(" enter your subject1 marks : "))
sub2 = int(input(" enter your subject2 marks : "))
sub3 = int(input(" enter your subject3 marks : "))
sub4 = int(input(" enter your subject4 marks : "))
sub5 = int(input(" enter your subject5 marks : "))

percentage = ((sub1 + sub2 + sub3 +sub4 + sub5) / 500 )*100

if(percentage > 80):
    print(f"percentage = {percentage} first Class , Congratulation.....!")
elif(percentage<80 and percentage>60):
    print(f"percentaGE ={percentage} Second class ")
else:
    print("All clear the semister")