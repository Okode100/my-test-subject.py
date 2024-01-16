hrs = input("Enter Hours:")
h = float(hrs)
rts = input("Enter Rates:")
r = float(rts)
#xhr = r * h
if h > 40:
    xhr = r * h
    otp = (h - 40.0) * (r * 0.5)
    xp = xhr + otp
    print("Pay:",xp)
else:
    print("Pay:",xp)
