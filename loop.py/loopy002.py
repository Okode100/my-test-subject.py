largest = None
smallest = None
while True:
        num = input("Enter a number:")
        if num == "done":
            break
        try:
            inx = int(num)
            if largest is None or inx > largest:
                largest = inx
            elif smallest is None or inx < smallest:
                smallest = inx
        except:
            print("Invalide input")
            continue
Avr = largest/smallest
print("Maximum is:",largest)
print("Minimum is:",smallest)
print("Averqge is:",largest/smallest)
print("Percentile is:",largest% Avr)
