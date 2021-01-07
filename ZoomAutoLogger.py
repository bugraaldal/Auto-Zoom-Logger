import pyautogui
import time
from datetime import datetime
import os
import pandas as pd
from pyscreeze import ImageNotFoundException
os.chdir("/home/buura/Desktop/Python/Zoom")
# Based on Linux operating systems


def join(entering_first, Run, id, parola):  # main function
    while Run:
        # Opens the Zoom app from the console. You must change this one to make it work on your computer
        os.system(
            "/var/lib/snapd/desktop/applications/zoom-client_zoom-client.desktop")
        time.sleep(10)
        if entering_first:  # Zoom has a problem. It crashes when at first. So I'm doing executing the starting part two times.
            # Kills the Zoom app and exits from the terminal
            os.system("pkill zoom")
            os.system("exit")
            time.sleep(5)
            entering_first = False
            continue
        # Locates the buttons and opens the meeting
        time.sleep(10)
        joinButton = pyautogui.locateCenterOnScreen("join_a_meeting.png")
        pyautogui.moveTo(joinButton)
        time.sleep(2)
        pyautogui.click()
        time.sleep(2)
        idBar = pyautogui.locateCenterOnScreen("idBar.png")
        pyautogui.moveTo(idBar)
        time.sleep(2)
        pyautogui.click()
        time.sleep(5)
        pyautogui.write(id)
        time.sleep(2)
        # Chcking the boxes in order to not connect our camera and microphone
        buttons = pyautogui.locateAllOnScreen("clickBox.png")
        for button in buttons:
            pyautogui.moveTo(button)
            pyautogui.click()
            time.sleep(3)
        join2nd = pyautogui.locateCenterOnScreen("joinbl.png")
        pyautogui.moveTo(join2nd)
        pyautogui.click()
        time.sleep(5)
        pyautogui.write(parola)
        time.sleep(5)
        pyautogui.press("enter")
        Run = False


# Adding the weekdays to make the program be able to work on a weekly basis schedule.
weekdays = ["Monday", "Tuesday", "Wednesday",
            "Thursday", "Friday", "Saturday", "Sunday"]

# An excel file which includes the starting and the ending time, ID, parola and the weekday of the meeting
timing = pd.read_csv("/home/buura/Desktop/Python/Zoom/ZoomSchedule.csv")
print(timing)
while True:
    # Getting the local time from the computer
    t = time.localtime()
    now = time.strftime("%H:%M:%S", t)
    week = datetime.now().weekday()
    # If the local time matches the starting hour and the weekday, executes the command
    if now in str(timing["time"]) and weekdays[week] in str(timing["day"]):
        row = timing.loc[timing["time"] == now]
        m_id = str(row.iloc[0, 1])
        m_pswd = str(row.iloc[0, 2])
        join(True, True, m_id, m_pswd)
        time.sleep(40)
        print("Signed In")
    # If the local time matches the ending hour, kills the app
    if now in str(timing["end"]):
        os.system("pkill zoom")
