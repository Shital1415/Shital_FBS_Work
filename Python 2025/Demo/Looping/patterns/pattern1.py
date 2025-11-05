'''
A B C D E 
B C D E 
C D E
D E
E
'''

for i in range(1,6):
    for j in range(64+i,70):
        print(chr(j),end=' ')
    print( )