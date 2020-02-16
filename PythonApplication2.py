from datetime import datetime
usersyear = int(input("name the year(yyyy)"))
while True:
     usersmonth = int(input("name the month(mm)"))
     if (usersmonth>0 and usersmonth<13): #swsta inputs check
        break
while True:
    usersdate = int(input("name the date (dd)"))
    if (usersmonth==1 or usersmonth==3 or usersmonth==5 or usersmonth==7 or usersmonth==8 or usersmonth==10 
        or usersmonth==12): #31 meres se ena mhna check
         if (usersdate>0 and usersdate<32):
             break
    elif (usersmonth==2): #disekto etos check
        if (( usersyear%400 == 0)or (( usersyear%4 == 0 ) and ( usersyear%100 != 0))):
           if (usersdate>0 and usersdate<30):
             break
        else:
           if (usersdate>0 and usersdate<29):
             break
    else : #30 meres ston mhna check
        if (usersdate>0 and usersdate<31):
             break

f_date = datetime(usersyear, usersmonth, usersdate, 00, 00, 00) #h hmeromhnia xrhsth
if (usersmonth==12): #check gia dekevrio,oytws wste na mhn exoyme thema sth metrhsh twn merwn toy mhna
    nextmonth=1
    usersnextyear=usersyear +1
else :
   nextmonth=usersmonth + 1
   usersnextyear=usersyear

g_date = datetime(usersyear,usersmonth, 1, 00, 00, 00) #afairoume ton mhna toy xrhsth
g_date2 = datetime(usersnextyear,nextmonth, 1,00,00, 00) # me ton epomeno mhna gia na 
                                                         #vroume poses meres exei
import datetime 
now = datetime.datetime.now()

from datetime import datetime #h shmerinh hmeromhnia
l_date = datetime( now.year, now.month, now.day, now.hour, now.minute, now.second)
delta = f_date - l_date #afairesh meras toy xrhsth me shmerinh hmeromhnia
print(delta) #apotelesma se meres kai wres,lepta,deyterolepta
delta2 = g_date2 - g_date #afairesh gia na vroume tis meres
print("οι μερες του συγκεκριμενου μηνα ειναι :",delta2.days) #apotelesma ypologismou se meres
