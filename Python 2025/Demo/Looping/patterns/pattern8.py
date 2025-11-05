'''
      *
     **
    ***
   ****
  *****
  '''

for i in range(1,6):
    for j in range (1,7-i):   #### this for decremental pattern 
        print(" ",end= '')
    for j in range (1,i+1):     ###this is for incremental pattern
        print("*",end= '')
        
    print()