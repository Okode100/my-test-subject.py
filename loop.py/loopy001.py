largest = None
smallest = None

while True:
        num = input("Enter a number: ")
        if num == "done":
            break
        try:
            inx = int(num)
            if largest is None or inx > largest:
                largest = inx
            if smallest is None or inx < smallest:
                smallest = inx
        except ValueError:
            print("Invalide input")

if largest is not None:
    print("Maximum is:",largest)

if smallest is not None:
    print("Minimum is:",smallest)
