import re
in_file = input("Enter the file name:")
open_file = open(in_file)

count = 0
for line in open_file:
    line = line.rstrip()
    #if line.startswith("From"):
    word = line.split()
    if len(word) > 2 and re.search(r'[\s@.+\s*]',word[1]):
        print(word[1])
        count +=1

print("There were", count."lines in the file with 'From' as the first word" )
