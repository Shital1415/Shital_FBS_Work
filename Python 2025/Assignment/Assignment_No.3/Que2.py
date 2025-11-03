'''2. Write a program to input any alphabet and check whether it is vowel or consonant.'''

#take i/p from user
character = str(input("enter the single character : "))

# for uppercase letter we use the lower() to convert the A---a ,Z--->z
char = character.lower()

if(char == 'a' or char == 'e'or char == 'i' or char == 'o' or char == 'u'):
    print(f"the give character { char } is vowel")
else:
    print(f"the give character { char } is consonant")
