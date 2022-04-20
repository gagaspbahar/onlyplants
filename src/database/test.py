import datetime

def changeDateFormat(dateNow) :
    return datetime.datetime.strptime(dateNow, '%d/%m/%Y').strftime('%Y-%m-%d')

print (changeDateFormat("04/01/2020"))

