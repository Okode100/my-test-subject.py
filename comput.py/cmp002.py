sh = input("Enter Hours:")
sr = input("Enter Rates:")
fh = float(sh)
fr = float(sr)
def computepay(hours,rate):
    if hours > 40:
        reg = rate * hours
        otp = (hours - 40.0) * (rate *0.5)
        pay = reg + otp
    else:
        pay = hours * rate
    return pay


xp = computepay(fh,fr)


print("pay",xp)
