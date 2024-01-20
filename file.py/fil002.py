fname = input("Enter file name: ")
fh = open(fname)
count=0
lz = 0
for lx in fh:
    ln = lx.strip()
    if not ln.startswith("X-DSPAM-Confidence:"):
        continue
    else:
        ly = float(ln[19:])
        lz += ly

        count += 1


avg = (lz/count)
print("Average spam confidence:", avg)
