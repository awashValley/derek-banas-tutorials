import re
# import sys

fl = open('randomcharacters.txt')

strToSearch = ""

for line in fl:
    strToSearch += line
    print(strToSearch)

# pattFinder = re.compile('b3b2c', re.IGNORECASE)      # doesn't work
# pattern = "b3b2c"
# pattFinder = re.compile(pattern)

## any letter
# pattFinder = re.compile('[a-z]', re.IGNORECASE)

## any random search
# pattFinder = re.compile('[#$\*^?0-9]', re.IGNORECASE)

## specific pattern
pattFinder = re.compile('\d\D\s\S.\W\w', re.IGNORECASE)

# findPatt = re.match(pattFinder, strToSearch)
findPatt = re.findall(pattFinder, strToSearch)

if(findPatt):
    # print(findPatt.group())
    for i in findPatt:
        print(i)
        # print(i, end="")      # doesn't work
else:
    print("Nothing Found")
