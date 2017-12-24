from datetime import *
def date_range(date1,date2):
     for i in range(int((date2-date1).days)+1):
          print(date1+timedelta(i))

start_date = date(2015,12,20)
end_date = date(2016,1,11)

date_range(start_date,end_date)
