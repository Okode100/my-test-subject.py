fhand = open('mbox-short.txt')
counts = dict()
for line in fhand:
    words = line.split()
    for word in words:
        word.startswith('From')
        counts[word] = counts.get(word,0)+1

lst = list()
for key, val in counts.items():
    newtup = (val, key)
    lst.append(newtup)

lst = sorted(lst, reverse=True)

for val, key in lst[:10]:
    print(key,val)
