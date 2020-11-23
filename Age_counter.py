import calendar,datetime

def larba_theory(birthaday):
    x = datetime.datetime.now()
    all_for=str(int(str(x.year)+str(x.month)+str(x.day))-int(birthaday))
    return all_for[:2]

Dob=input("DOB yyyy/mm/dd:")
print(larba_theory(Dob))
