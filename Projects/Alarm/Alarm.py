import datetime
from playsound import playsound

alarmhour = int(input("Enter Hour: "))
alarmMin = int(input("Enter Minutes: "))
alarmAMPM= input("am / pm: ")
print("Alarm has been set...")

if alarmAMPM == "pm":
    alarmhour +=12

while True:
    if alarmhour==datetime.datetime.now().hour and alarmMin==datetime.datetime.now().minute:
        print("Playing.....")
        playsound("C:\\Users\\india\\Desktop\\Python\\Projects\\Alarm\\alarm.mp3")
        print("Thanks for using! :)")
        break
