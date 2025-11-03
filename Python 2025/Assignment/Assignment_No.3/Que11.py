'''
11. Accept age of five people and also per person ticket amount and then calculate total 
amount to ticket to travel for all of them based on following condition : 
a. Children below 12 = 30% discount 
b. Senior citizen (above 59) = 50% discount 
c. Others need to pay full.
'''
i = int(input("enter no.of passenger :"))
sum = 0
###initialize the tickect cost in rupees
child_tick = 15
old_people = 10
young_people = 20
for i in range(1,i+1):
    age = int(input("what is your age :"))
    if(age<12 or age >59 or age in range(12,59)):
        sum += child_tick
print('total amount to ticket to travel for all of them ' , sum)
print("have a nice day")

