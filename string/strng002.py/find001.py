text = "X-DSPAM-Confidence:    0.8475"
txt = text.find(':')
po = text[txt+1:]
pos = float(po)
print(pos)

str1 = "Hello"
str2 = 'there'
bob = str1 + str2
print(bob)

smallest_so_far = -1
for the_num in [9, 41, 12, 3, 74, 15] :
   if the_num < smallest_so_far :
      smallest_so_far = the_num
print(smallest_so_far)
tot = 0
for i in [5, 4, 3, 2, 1] :
    tot = tot + 1
print(tot)

tot = 0
for i in [5, 4, 3, 2, 1] :
    tot = tot + 1
print(tot)

n = 0
while n > 0 :
    print('Lather')
    print('Rinse')
print('Dry off!')
