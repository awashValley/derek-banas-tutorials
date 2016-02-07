import re

fl = open('randomcharacters.txt')

strToSearch = ""

for line in fl:
    strToSearch += line
    print(strToSearch)
