import re
#pull first 3 numbers then the next 3 then the last four of a phone number.
phoneRegex = re.compile(r'\d{3,}.\d{3,}.\d{4,}')

#pull the word before the @ sign then the word after then the (.) then the word after the period.
emailRegex = re.compile(r'\w+\@\w+\.+\w{3,}')

#filename
filename = 'pandetxt'

#open file
with open(filename) as f:

    #vieual effects
    print('Phone Numbers-')

    #loop through the file
    for p_num in f:

        # run the regex
        test1 = phoneRegex.findall(p_num)

        # print the regex and remove any white spaces
        for result in test1:
            print(result.rstrip())

#open file
with open(filename) as f:

    # vieual effects
    print('Emails-')

    # loop through the file
    for e_addr in f:
        # run the regex
        test2 = emailRegex.findall(e_addr)

        # print the regex and remove any white spaces
        for result in test2:
            print(result.rstrip())