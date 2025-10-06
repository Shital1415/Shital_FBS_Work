#calculate area and perimeter

l=int(input("Enter the Length of rectangle : "))
b=int(input("Enter the breadth of rectangle : "))
r=int(input("Enter the radius of Semicircle : "))

#calculate area 
area_of_rectangle=l*b
area_of_semicircle=(3.14*r*r)*1/2
total_area = area_of_rectangle + area_of_semicircle

#calculate perimeter of following dia.
perimeter_of_rect = 2*(l + b)
perimeter_of_semicircle = (3.14 * r)+(2*r)
total_peri = perimeter_of_rect + perimeter_of_semicircle

#display O/P

print(f'the total area of diagram = {total_area} .')
print(f'the total perimeter of diagram = {total_peri} .')
