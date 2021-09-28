from os import system
import time
import datetime

print("NOTE: THIS WILL NOT WORK ON REPL OR A WINDOWS COMPUTER. THIS HASN'T BEEN TESTED SO IT MAY NOT WORK ON OPERATING SYSTEMS WITHOUT A macOS TERMINAL.\n")

local_time = datetime.datetime.now()
current_time = local_time.strftime("%H")

if current_time <= "11":
    print("Good morning, sir!")
    system("say good morning, sir!")
elif current_time >= "12":
    print("Good afternoon, sir!")
    system("say good afternoon, sir!")
elif current_time >= "16":
    print("Good evening, sir!")
    system("say good evening, sir!")
elif current_time >= "20":
    print("Hello, sir!")
    system("say hello, sir!")
 
time.sleep(1)

print("The date is " + local_time.strftime("%A %B %d, %Y"))
system("say the date is " + local_time.strftime("%A %B %d, %Y"))

time.sleep(1)

print("The time is " + local_time.strftime("%I:%M %p"))
system("say the time is " + local_time.strftime("%I:%M %p"))

time.sleep(1)

system("say what is your name")

name = input("Hello! What is your name? Enter here: ")

if name == "":
    system("say name parameter is blank. anyway, lets continue")
else:
    system("say hello, " + name)

time.sleep(1)
system("say how are you feeling today? 1 amazing, 2 good, 3 okay, 4 bad, or 5 miserable")
feeling = input("How are you feeling today? (1)amazing, (2)good, (3)okay, (4)bad, or (5)miserable? ")

if feeling == "1":
    print("I am happy to hear that!")
    system("say i am happy to hear that!")
elif feeling == "2":
    print("Nice!")
    system("say nice!")
elif feeling == "3":
    print("Okay!")
    system("say okay")
elif feeling == "4":
    print("That's okay. Hopefully you'll feel better!")
    system("say thats okay. hopefully youll feel better")
elif feeling == "5":
    print("I am very sorry to hear that. ")
    system("say i am very sorry to hear that")
else:
    system("say invalid parameter")
    raise Exception("Invalid paramater.")

time.sleep(1)
system("say anyway, thank you for using me")
print("\nAnyway, thank you for using me.")

system("say bye bye, " + name + "!")

if name == "":
    print("Bye bye!")
else:
    print("Bye bye, " + name + "!")
exit()
