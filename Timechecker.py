import os
import datetime

timeset = datetime.datetime.now()

print("Note: press 'ctrl' or 'control' (for mac) + 'c' to terminate program. You may need to do it twice if you want to do it while the voice is talking.")

os.system("say welcome!")
os.system("say the date is " + timeset.strftime("%A %B %d, %Y"))
os.system("say the time is " + timeset.strftime("%I:%M %p"))

while True:
    input("Press 'enter'  or 'return' to see time...")
    os.system("say the time is " + timeset.strftime("%I:%M %p") + " and " + timeset.strftime("%S") + "seconds")
    print("The time is " + timeset.strftime("%I:%M:%S %p"))
