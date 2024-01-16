score = input("Enter score")
scr = float(score)
#scr = range(int(0.00),int(1.00))
if scr >= 0.0 <=1.0:
        print("Grade is:")
        if scr > 1.0:
            print("Grade does not exist")
        else:
            if scr >= 0.9:
                print("A")
            else:
                if scr >= 0.8:
                    print("B")
                else:
                    if scr >= 0.7:
                        print("C")
                    else:
                        if scr >= 0.6:
                            print("D")
                        else:
                            if scr >= 0.00:
                                print("F")
