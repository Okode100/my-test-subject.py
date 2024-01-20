file = input("Enter file:") #user intput
opn = open(file) #opening thr file name mbox-short.requestContext
read = opn.read() # reading the content of the file
right_strip = read.rstrip()
email = dict() #creating a dictionary
for line in right_strip:
     if line.startswith('From'): #searching for the line that starts with 'From'
         word_split = line.split() #spliting the word
         next_word = word_split[1]
         email[next_word] = email.get(next_word,0) + 1
#finding the max
bigword = None
bigcount = None
for word_split, count in email.items():
    if bigcount is None or count > bigcount:
        bigword = next_word
        bigcount = count
print(bigword, bigcount)
print(line)
