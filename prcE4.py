import re

def change_data_format(dt):
    nr = re.compile(r'(\d{4})-(\d{1,2})-(\d{1,2})')
    return nr.sub(r'\3-\2-\1', dt)

dt1 = '2018-01-02'
print("org",dt1)
print("new",change_data_format(dt1))