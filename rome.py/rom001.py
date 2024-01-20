fname = input("Enter the file name:")
fopen = open(fname)
fsplit = fopen.read()
fstrip = fsplit.split()

flist = []
for word in fstrip:
    #word = fstrip.lower()
    if word is  fstrip:
        continue
    else:
        if not  fstrip:
            fstrip.append()

    fstrip.sort()


print(fstrip)
