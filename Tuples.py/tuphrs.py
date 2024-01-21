name = input("Enter file:")
if len(name)< 1:
    name = "mbox-short.txt"
handle = open(name)
#tp_read = handle.read()#print(tp_read)

count = {}
for line in handle:
    if line.startswith("From"):
        line = line.split()
        if len(line)> 5:
            time = line[5].split(".")
            hour = time[0]
            count[hour] = count.get(hour,0) + 1
            count +=1

for k,v in sorted(count.items()):
    print(k,v)
