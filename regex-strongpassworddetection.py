#Objective - A strong password is defined as one that is at least eight characters long, contains both uppercase and lowercase characters, and has at least one digit.

import re

#this is what we need ot be in the input to be true
requirements = "^.*(?=.{8,})(?=.*\d)(?=.*[a-z])(?=.*[A-Z])(?=.*[~!@#$%^&+=]).*$"
border = '++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++'

#pass in input for a strong password
passwd = input(border + '\*Please enter a password with the following requirements:\n*At least eight characters long*\n*Contains both uppercase and lowercase characters*\n*Has at least one digit*\n' + border)

#using the findall to check requirements to what we input
endResult = re.findall(requirements, passwd)

#printing whether it is valid or not
if (endResult):
    print('Valid Password')
else:
    print(border + 'Invalid Password\nRequirements listed below\n*At least eight characters long-\n*Contains both uppercase and lowercase characters-\n*Has at least one digit-\n' + border)
n w45