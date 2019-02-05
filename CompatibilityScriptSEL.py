'''
Austin Wong-Parker
Compatibility Report Script using Selenium, Pyautogui, & AutoIt

Project Start: 1/25/19

'''

# ----------------------------------------------------------
# These are the imported Methods for the script.
# ----------------------------------------------------------
import os
import time
import pyautogui
import webbrowser
import win32gui
from pywinauto import Application
from selenium import webdriver
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.ui import WebDriverWait # available since 2.4.0
from selenium.webdriver.support import expected_conditions as EC # available since 2.26.0
from selenium.webdriver.firefox.firefox_binary import FirefoxBinary
from selenium.webdriver.common.keys import Keys

# ----------------------------------------------------------
# These are self-made functions for the script.
# ----------------------------------------------------------

def maxFileRobo(): #function to open and maximize RoboScreenCapture
    os.system("\\\\sidewinder\SW_Vault\PENDING\_IO-Link_Devices\_Compatibility_Reports\Scripts\MaxRoboScreen.exe")

def doubleClick(): #simulate double-clicking the mouse
    pyautogui.PAUSE = 0
    pyautogui.click()
    pyautogui.click()
    pyautogui.PAUSE = 1

def tripleClick(): #simulate triple-clicking the mouse
    pyautogui.PAUSE = 0
    pyautogui.click()
    pyautogui.click()
    pyautogui.click()
    pyautogui.PAUSE = 1

def Highlighter(): #function to open highlighter in RoboCapture [Hard-coded]
    pyautogui.moveTo(13, 340)
    pyautogui.click()

def roboText(): #function to open text-maker in RoboCapture [Hard-coded]
    pyautogui.moveTo(60, 170)
    pyautogui.click()

def redCircle(): #function to open circle-maker in RoboCapture [Hard-coded]
    pyautogui.moveTo(35, 268)
    pyautogui.click()

def resetIOLinkMaster(): #function to allow pyautogui to reset the IO-Link Master [Hard-coded]
    '''
    -
    -
    -
    '''

def askIODDFinder(): #function to allow pyautogui
    '''
    -
    -
    -
    '''

def editroboText(): #function to change font, color, and style size
    pyautogui.PAUSE = 1
    pyautogui.moveTo(581, 345)
    pyautogui.click()
    pyautogui.moveTo(804, 315)
    pyautogui.PAUSE = 0
    pyautogui.click()
    pyautogui.click()
    pyautogui.PAUSE = 1
    pyautogui.hotkey('1')
    pyautogui.hotkey('2')
    pyautogui.moveTo(696, 377)
    pyautogui.click()
    pyautogui.moveTo(639, 527)
    pyautogui.click()
    pyautogui.hotkey('r')
    pyautogui.moveTo(880, 320)
    pyautogui.click()
    pyautogui.click()

def Transparent(): #function to turn on transparent background for text
    pyautogui.moveTo(630, 319)
    pyautogui.click()
    pyautogui.moveTo(735, 374)
    pyautogui.click()
    pyautogui.moveTo(591, 322)
    pyautogui.click()

def savePhotoFirst(): #function for the first time saving a photo from Robocapture
    pyautogui.hotkey('alt')
    pyautogui.hotkey('f')
    pyautogui.hotkey('a')
    pyautogui.moveTo(740, 255)
    pyautogui.click()
    pyautogui.moveTo(726, 274)
    pyautogui.click()
    pyautogui.hotkey('d')
    pyautogui.hotkey('d')
    pyautogui.hotkey('d')
    pyautogui.moveTo(627, 304)
    doubleClick()
    pyautogui.moveTo(835, 428)
    pyautogui.click()

def savePhoto(): #function for saving photos from RoboCapture
    pyautogui.hotkey('alt')
    pyautogui.hotkey('f')
    pyautogui.hotkey('a')
    pyautogui.press('enter')

def minRobo(): #function for minimizing RoboCapture
    pyautogui.moveTo(1324, 12)
    pyautogui.click()

def reopenRobo(): #function for re-opening RoboCapture
    pyautogui.moveTo(659, 881) #This will serve as a dual-purpose: opening the RoboScreenCapture Program and moving the mouse out of the Screenshot
    pyautogui.click()

def comtrolRobo(): #function for moving cursor to top-left screen where the comtrol icon is
    pyautogui.moveTo(0, 75)

def midDiagRobo(): #function for moving cursor to port 2 (right side) for the diagnostics page
    pyautogui.dragTo(866, 856)
    pyautogui.click()

def openEditconfigMid(): #function for moving cursor to opened edit for configuration page
    pyautogui.dragTo(960, 857)
    pyautogui.click()

def closedEditconfigMid(): #function for moving cursor to closed edit for configuration page
    pyautogui.dragTo(956, 857)
    pyautogui.click()

# ----------------------------------------------------------------------------
# Starting of the script; user will need to fill out the following questions.
# ----------------------------------------------------------------------------
print('  ')
print('---Script Starting---')
print('Fill out information below')
print('  ')

# ----------------------------------------------------------
# Declaring Variables + asking questions for user
# ----------------------------------------------------------

nameOfDevice = input("Please enter the name of your device: ") # User enters name of Device
portName = input("Please enter port name for your device (Less than 23 characters): ") # User enters friendly-port name of Device

# Welcome Script [AutoIt]
os.system("\\\\sidewinder\SW_Vault\PENDING\_IO-Link_Devices\_Compatibility_Reports\Scripts\Welcome.exe")

# Create a new instance of the Firefox driver
driver = webdriver.Firefox()

# ----------------------------------------------------------
# SCRIPT IS NOW ACTIVE
# ----------------------------------------------------------

# Step 1: go to the IO-Link Master
print('Step 1')
driver.get("http://10.8.14.84")

# Step 2: Make browser 80% magnifer
print('Step 2')
pyautogui.hotkey('ctrl', '-')
pyautogui.hotkey('ctrl', '-')

# Step 3: go to advanced | software
print('Step 3')
driver.get("http://10.8.14.84/Software")

# Step 4: get window size
print('Step 4')
print(" ")
print(driver.get_window_size())
print("Script: Making maximum window size.")
driver.maximize_window()

# Step 5: Taking screenshot 1 (Page 3)
print('Step 5')
maxFileRobo()
time.sleep(1)
pyautogui.hotkey('ctrl', 'shift', 'r')
pyautogui.PAUSE = 1
pyautogui.moveTo(543,0)
pyautogui.hotkey('ctrl', 'shift', 'r')
pyautogui.moveTo(0,75) #Near Comtrol Icon
pyautogui.dragTo(869, 854, 0.5, button='left')
pyautogui.click()

# Step 6: Edits to Screenshot 1 (Page 3)
print('Step 6')
time.sleep(2)
Highlighter()
pyautogui.moveTo(532, 271)
pyautogui.dragTo(590, 402)
pyautogui.click()
roboText()
pyautogui.moveTo(605, 321)
pyautogui.dragTo(854, 418, 0.5, button='left')
editroboText()
Transparent()
pyautogui.typewrite('Firmware (images and applications) can be upgraded in the field or before deployment.')
pyautogui.moveTo(682, 576) #Press OK in Edit Text Screen
pyautogui.click()
savePhotoFirst()
minRobo()

# Step 7: Taking screenshot 2 (Page 4)
print('Step 7')
driver.get("http://10.8.14.84/IOLink/Diag")
pyautogui.moveTo(1194, 192)
pyautogui.click()
reopenRobo()
pyautogui.hotkey('ctrl', 'shift', 'r')
comtrolRobo()
midDiagRobo()

# Step 8: Edits for screenshot 2 (Page 4)
print('Step 8')
time.sleep(2)
Highlighter()
pyautogui.moveTo(385, 329)
pyautogui.dragTo(542, 462)
pyautogui.moveTo(386, 568)
pyautogui.dragTo(457, 622)
pyautogui.moveTo(385, 729)
pyautogui.dragTo(446, 782)
pyautogui.click()
roboText()
pyautogui.moveTo(468, 219)
pyautogui.dragTo(925, 259, 0.5, button='left')
editroboText()
pyautogui.typewrite('This does not display the complete Diagnostics page.')
pyautogui.moveTo(682, 576) #Press OK in Edit Text Screen
pyautogui.click()
pyautogui.moveTo(545, 543)
pyautogui.dragTo(918, 602, 0.5, button='left')
pyautogui.typewrite('Notice that the IO-Link Master negotiates the Device Minimum Cycle Time and the PDI data is valid.')
pyautogui.moveTo(682, 576) #Press OK in Edit Text Screen
pyautogui.click()
savePhoto()
minRobo()

# Step 9: Taking Screenshot 3 (Page 5)
print('Step 9')
driver.get("http://10.8.14.84/IOLink/Settings")
pyautogui.moveTo(714, 271)
pyautogui.click()
pyautogui.moveTo(559, 741)
pyautogui.click()
pyautogui.press('down')
pyautogui.press('enter')
pyautogui.moveTo(566, 301)
tripleClick()
pyautogui.typewrite(portName)
reopenRobo()
pyautogui.moveTo(721, 279)
pyautogui.hotkey('ctrl', 'shift', 'r')
comtrolRobo()
openEditconfigMid()

# Step 10: Edits for Screenshot 3 (Page 5)
print('Step 10')
time.sleep(2)
redCircle()
pyautogui.moveTo(792, 271)
pyautogui.dragTo(833, 325)
pyautogui.moveTo(620, 745)
pyautogui.dragTo(673, 770)
pyautogui.moveTo(1000, 272)
pyautogui.dragTo(1047, 305)
time.sleep(2)
Highlighter()
pyautogui.moveTo(627, 311)
pyautogui.dragTo(721, 329)
pyautogui.click()
roboText()
pyautogui.moveTo(583, 199)
pyautogui.dragTo(796, 251, 0.5, button='left')
pyautogui.typewrite('Click SAVE after making configuration changes.')
pyautogui.moveTo(682, 576) #Press OK in Edit Text Screen
pyautogui.click()
roboText()
pyautogui.moveTo(824, 199)
pyautogui.dragTo(1032, 261, 0.5, button='left')
editroboText()
pyautogui.typewrite('Click EDIT to make configuration changes.')
pyautogui.moveTo(682, 576) #Press OK in Edit Text Screen
pyautogui.click()
savePhoto()
minRobo()
pyautogui.moveTo(721, 279)
pyautogui.click()

# Step 11: Taking Screenshot 4 (Page 6)
print('Step 11')
time.sleep(2)
pyautogui.hotkey('ctrl', 'r')
reopenRobo()
pyautogui.hotkey('ctrl', 'shift', 'r')
pyautogui.PAUSE = 3
comtrolRobo()
pyautogui.PAUSE = 1
closedEditconfigMid()

#Step 12: Edits for Screenshot 4 (Page 6)
time.sleep(2)
Highlighter()
pyautogui.moveTo(133, 623)
pyautogui.dragTo(841, 650)
pyautogui.click()
roboText()
pyautogui.moveTo(505, 197)
pyautogui.dragTo(922, 270, 0.5, button='left')
pyautogui.typewrite('You can refresh the web page to see that data storage has been uploaded to the IO-Link Master.')
pyautogui.moveTo(682, 576) #Press OK in Edit Text Screen
pyautogui.click()
savePhoto()
minRobo()
