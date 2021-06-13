from datetime import datetime, timedelta

# x = datetime(2020, 1, 2) # this is Thursday and week 1 in ISO calendar; should be 1 in custom calendar w/ week starting Thu
# y = datetime(2020, 1, 3) # this is Friday and week 1 in ISO calendar; should be 2 in custom calendar
# print(x)
# print(y)

def weeknum(dt):
    return dt.isocalendar()[1]

def myweeknum(dt):
    offsetdt = dt + timedelta(days=+3)  # you add 3 days to Mon to get to Thu 
    return weeknum(offsetdt)

# print(weeknum(x));
# print(myweeknum(x));

# print(weeknum(y));
# print(myweeknum(y));


dt = datetime(2019, 12, 17) # this is Friday and week 1 in ISO calendar; should be 2 in custom calendar

# print(myweeknum(dt))
f = open("demofile2.txt", "a")

rw = ""
for i in range(400):
    offsetdt = dt + timedelta(days= (i+3))
    wknum = myweeknum(offsetdt)
    op = str(datetime.date(offsetdt)) + "|" + 'Week - ' + str(wknum)
    if rw == "":
        rw = op
    else:
        rw = rw + "|" + op

    if (i+1) % 7 == 0:
        f.write(rw + '\n')
        rw = ""
        # rw = rw + "\n" 
        # print(op)
       
f.close()

# #open and read the file after the appending:
# f = open("demofile2.txt", "r")
# print(f.read())