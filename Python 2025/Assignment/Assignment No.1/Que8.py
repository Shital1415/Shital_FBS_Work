# convert days into years, weeks and days
# take i/p for user
days = int(input("Enter days  : "))

#calulation
years = days // 365

days = days % 365

weeks = days // 7

days = days % 7

print(f'years : {years} , weeks : {weeks} , days : {days}')