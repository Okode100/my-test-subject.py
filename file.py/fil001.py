count = 0
total_confidence = 0.0
fname = input("Enter file name:")
fh = open(fname)
for line in fh:
    if not line.startswith("X-DSPAM-Confidence"):
        continue
    else:
        confidence = float(line[19:])
        total_confidence += confidence
        count +=1
average_confidence = total_confidence/count
print("Average spam confidence:", average_confidence)
