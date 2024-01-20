def computepay(Hours, Rates):
    print("In computepay", Hours, Rates)
    if Hours > 40:
        chr = Hours * Rates
        otp = (Hours - 40.0) * (Rates * 0.5)
        Pay = chr + otp
    else:
        Pay = Rates * Hours
        print("Returning:",Pay)
        return Pay

hrs = input("Enter Hours:")
rts = input("Enter Rates:")
hr = float(hrs)
rs = float(rts)

xp = computepay(hr,rs)

print("pay:", xp)
