"""
Project Title: Zoom Class Automation
Author: Aryan Rastogi

Description:
This project helps individuals to automatically join scheduled zoom meetings by entering the meeting details
beforehand.
"""


import webbrowser
import time
import datetime

link = []
start_time = []


def join_meeting(link):
    webbrowser.open(link)

print("\n")
print("HELLO USER!!\n")
print("* Please enter the links and start time of the meetings in ASCENDING ORDER of the start time.")
print("* Make sure that the meetings don't overlap i.e. another meeting starts only after the first one ends!!")
print("* Enter time in 24 hr format i.e 2:30 pm should be entered as 14:30.")
print("* You will be asked to enter the delay time in minutes eg. If the delay is 5, then the meetings will be joined 5\
 minutes later than the specified start time.\n")
print("* Press \"Ctrl+C\" to terminate the batch file.\n")

num_classes = int(input("Enter the number of classes today: "))
print("\n")
for i in range(num_classes):
    start_time.append(list(map(int, input("Enter start time of meeting in 24 hr format (eg. 1:30 pm is 13:30): ").split(":"))))
    link.append(input("Enter meeting link: "))
    print("\n")

start_wait = int(input("Enter the DELAY to join the meeting in minutes : "))   # The next meeting will start specified minutes late to ensure that the previous meeting has ended.
print("\n")
i = 0
while datetime.datetime.now().hour <= start_time[-1][0]+1 and i < len(start_time):
    current_time = datetime.datetime.now()
    if current_time.hour == start_time[i][0] and current_time.now().minute == start_time[i][1]+start_wait:
        join_meeting(link[i])
        print("Meeting No. {} has started".format(i+1))
        time.sleep(60)
        i += 1
