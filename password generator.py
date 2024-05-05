import random

upper_case="ABCDEFGHIJKLMNOPQRSTUVWXYZ"
#converting the upwwer case to lowercase

lower_case=upper_case.lower()
symbols="!@#$%^&*"
#password should contain upper,lower,symbols

combination=upper_case+lower_case+symbols

amount=int(input('How many passwords do you need? '))
pwd_len=int(input('Prompt the length of the password: '))
#generates amount no. of passwords

for i in range(amount):
    password="".join(random.sample(combination,pwd_len))
    print(password)