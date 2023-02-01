def stndrdth(oint):
    if oint in (1, 21, 31):
        return "st"
    elif oint in (2, 22):
        return "nd"
    elif oint in (3, 23):
        return "rd"
    else:
        return "th"

def simpleUSDateFormat(odate, mode):
    mdict0 = {1: "Jan", 2: "Feb", 3: "Mar", 4: "Apr", 5: "May", 6: "Jun", 7: "Jul", 8: "Aug",
              9: "Sep", 10: "Oct", 11: "Nov", 12: "Dec"}

    tday = str(odate.day) + stndrdth(odate.day)

    if mode == 0:
        return mdict0[odate.month] + "." + tday
    else:
        return mdict0[odate.month] + "." + tday + "," + str(odate.year)