import re
filename = 'pandetxt'
with open(filename, 'r'):
    data = filename.read()  # produces single string
print(data)
dateRegex = re.compile(r'(\d(1,2))\\(\d(1,2))\\(\d(4))')

