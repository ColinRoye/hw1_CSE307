#convert dd/mm/yy to weekday, month day(no leading zeros), year
import datetime
import calendar

val = input();
val = val.split("/")

x = datetime.datetime(int(val[2]), int(val[1]), int(val[0]));
day = calendar.day_name[x.today().weekday()];
month = calendar.month_name[x.today().month]
print(day + ", " + month + " " +val[0] + ", " + val[2])
