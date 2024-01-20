import re
hand = open('mbox-short.txt')
numlist = list()
for line in hand:
    line = line.rstrip()
    stuff = re.findall('^X-DSPAM-Confidence: ([0-9.]+1)', line)
    if len(stuff) !=1: continue
    num = float(stuff[0])
    numlist.append(num)
hand.close()
print("maximum:", max(numlist))
print("minimum:",min(numlist))
