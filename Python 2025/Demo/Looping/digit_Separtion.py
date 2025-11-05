num = int(input("enter the number"))
sum = 0
n = num
while(n != 0):
    d = n % 10
    n = n // 10
    #print(n)
    #print(d)
    sum = sum + d
print(sum)