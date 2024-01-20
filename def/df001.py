def computepay(h, r):
    print("computepay", hrs, rts)
    if hrs > 40.0:
        xhr = r * h
        otp = (hrs - 40.0) * (rts * 0.5)
        xp = xhr + otp
        #print("Pay:",xp)
    else:
        xp =xhr + otp
        print("Returning", xp)
        return xp
hrs = input("Enter Hours:")
h = float(hrs)
rts = input("Enter Rates:")
r = float(rts)
x = computepay(hrs,rts)
print("Pay",xp)
