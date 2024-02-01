import re
fname = input("Enter file name:")
if len(fname) < 1:
    fname = "mbox-short.txt"
fh = open(fname)
count = {}
highest_count = None
for line in fh:
    line.rstrip()
    if line.startswith("From"):
        word = line.split()
        if len(word) >2 and re.search(r'[\s@.+\s*]',word[1]):
            count[word[1]] = count.get(word[1], 0) + 1
            if highest_count is None or count[word[1]] > count.get(highest_count,0):
                #count = highest_count
                highest_count = word[1]
print("There wwere", count[highest_count],"lines in the file with 'From' as the as the first word")
