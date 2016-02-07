import re

fl = open('names.txt')

strToSearch = ""

for line in fl:
    strToSearch += line

print(strToSearch)

## search for Jennifer
# pattFinder = re.compile('Je[nnifer|nny|n]{1,6}\s\w+\s')
pattFinder = re.compile('Je[nifery]{1,6}\s\w+\s')       ## works fine too
findPatt  = re.findall(pattFinder, strToSearch)

if(findPatt):
    for i in findPatt:
        print(i)
else:
    print("Nothing Found")
