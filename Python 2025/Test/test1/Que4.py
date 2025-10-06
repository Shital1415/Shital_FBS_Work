#calculate the cost 

interior_cost_perRoom = 20000
exterior_cost_perRoom = 15000

wall=int(input("enter the length of wall in Sq.Foot "))

#operation
area_of_oneRoom = wall**2

#for each room interior painting cost = 20000
interior_painting_cost = (2*area_of_oneRoom)*interior_cost_perRoom
#Display O/P
print(area_of_oneRoom)
print(f"the total interior painting cost of TWO rooms : {interior_painting_cost}")

##Exterior Painting:
Distance_for_exterior = area_of_oneRoom - wall
#for Both room Exterior painting 
Exterior_painting_cost = Distance_for_exterior*exterior_cost_perRoom
print(f"the total interior painting cost of TWO rooms : {Exterior_painting_cost}")
