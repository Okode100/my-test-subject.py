d = {'a':10, 'b':1, 'c':22}
t = sorted(d.items())
print(t)

for k,v in sorted(d.items()):
    print(k,v)

tmp = list()
for k,v in sorted(d.items()):
    tmp.append((v,k))
    print(tmp)
