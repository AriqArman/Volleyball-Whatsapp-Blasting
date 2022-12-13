import pywhatkit as py
import datetime as datetime

time = "5:30 p.m - 8:30 p.m" 
venue = "Educity Stadium"
date_time = datetime.datetime.now()
date = date_time.strftime("%x")
group_id = "EVjKe7MUA1F78OBe6PqUws"
message = f" Volleyball Session {date}\n Venue: {venue} \n Time: {time} or so \n \n 1. "

#wait time is how long the program will wait for whatsapp to load / send message
#close time is how long the program will wait after sending the message

py.sendwhatmsg_to_group(group_id, message, time_hour= 15, time_min= 19, wait_time= 7, tab_close= True, close_time= 5)

