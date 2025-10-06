# Compound Interest
p=int(input("Enter Principal Amount : "))
r=int(input("Enter Annual rate in %  : "))
t=int(input("Enter time : "))

#convert R from % to decimal
R=r/100

#final amount = P*(1+r)^T
final_amount = p*(1+R)**t

#calculate CI
CI = final_amount - p
print("compound interest is " , CI)