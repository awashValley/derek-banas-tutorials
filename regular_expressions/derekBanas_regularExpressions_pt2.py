## suppose we would like to search for Jennifer or Jen or Jenny
##  '(Jennifer | Jen | Jenny)\b\w+\b' is the same as 'Je(nnifer|nny|n){1,6}\s\w+\s'
##  'Je(nnifer|nny|n){1,6}\s\w+\sJe(nnifer|nny|n)' is the same as 'Je(nnifer|nny|n){1,6}\s\w+\s1'
##              Here the number '1' represents the value in the bracket.
##              'Je(nnifer|nny|n){1,6}(\s\w+)\s(\s\w+)' is the same as 'Je(nnifer|nny|n){1,6}(\s\w+)\s\2'

## searching any sentence that starts with Cat.
##      '(^Cat\s\w+$)' - a sentence that starts with Cat (but not Cats because of \s). The $ signifies end of a sentence.
##      '(^Cat\s.+$)'  - the same as above. The DOT represents anything exept a new line.

## import 're' library
import re

## import the file
fl = open('randomcharacters.txt')

## create empty object
strToSearch = ""

## loop through the strings
for line in fl:
    strToSearch += line

print(strToSearch)
