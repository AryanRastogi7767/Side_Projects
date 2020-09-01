# Side_Projects

## ZOOM Class Automation
An automation script in python for automatically joining online classes using class links.

#### REQUIREMENTS:

 - Installed Python 3.5 or above (To Download: https://www.python.org/downloads/)
 - Installed datetime package (Paste this in CMD to install datetime package: pip3 install datetime)
 - Installed ZOOM Client. (To Download: https://zoom.us/download)
 
#### HOW TO RUN THE PROGRAM:

* Right-click on the zoom_automation.bat file and open it with notepad.
* Set the paths of python.exe and main.py in the batch file.
  * First Path - "Path to where python.exe is located"
   1. Search "python.exe" in your system and open file location. 
   2. Copy the path of the file in the batch file opened in the notepad.
  * Second Path - "Path to where the main.py is located"

* Run the `zoom_automation.bat` to run the batch file
* Finally after the cmd is opened read the instructions thoroughly and proceed by entering your
  zoom meeting info.
* Make sure you enter the meetings in ascending order of start time.
* Meeting time should be entered in 24 hr format, i.e. 1:30 pm is 13:30.
* You will be asked to enter a DELAY (in minutes) in joining the meeting.
  The delay is to ensure that the previous meeting has ended succesfully for
  the next meeting to start.
* Note that the next meeting will not start until the previous meeting has ended.
  so make sure that the current meeting ends on time for the next meeting to start.
  
#### MAKE SURE TO CONFIGURE ZOOM CLIENT SETTINGS AS:
![VIDEO CONFIG](https://github.com/AryanRastogi7767/Side_Projects/blob/master/Zoom%20Class%20Automation/zoom_vid.png)

![AUDIO CONFIG](https://github.com/AryanRastogi7767/Side_Projects/blob/master/Zoom%20Class%20Automation/zoom_audio.png)

#### FOR ANY QUERIES AND SUGGESTIONS: 
* Create an issue.
* Mail me at aryanrastogi97@gmail.com, I will try to reply as soon as possible.

#### FEATURES THAT MIGHT BE ADDED IN THE FUTURE:

- Joining class using meeting id and password.
- Joining classes smoothly even with unordered input of class details.
- Customizable program according to individuals timetable.

#### Do give a * if it helps you.
