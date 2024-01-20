import re

name = input("Enter the file name")
if len(name)<1:
    name = "mbox-short.txt"
handle = open(name)


count = {}
most_prolific = None

for line in handle:
    line = line.rstrip()
    if line.startswith("From "):
        words = line.split()
        if len(words) > 2 and re.search(r'[\s@.+\s*]',words[1]):
            #print(words)
            count[words[1]] = count.get(words[1],0)+ 1
            if most_prolific is None or count[words[1]] > count[most_prolific]:
                most_prolific = words[1]
                
print(most_prolific, count[most_prolific])
