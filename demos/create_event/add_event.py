from google_cred import Google
from calendar_obj.calender_obj import calendar_obj, date, time, event

mycal = calendar_obj()


myevent = event("My Python Event")


starttime = time(8,30)
startdate = date(2023, 4, 30)
myevent.set_start_time(startdate, starttime)

endtime = time(9)
enddate = date(2023, 4, 30)
myevent.set_end_time(enddate, endtime)

myevent.add_attendee('gene.luong@sjsu.edu')

mycal.add_event(myevent)