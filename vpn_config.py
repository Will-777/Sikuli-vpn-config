# SikuliX script ver 1.1.0
# VPN GUI automated config on Windows v0.1, Date 2017/4/13
# ---------------------------
# Task  : create VPN connection and shortcut 
# OS    : tested on Windows 8.1
# Input : user will be prompted to VPN info.
# ---------------------------
# 1) Set up the initial VPN configuration / SetUpNetConfig()
# 2) Update the VPN configuration with password and URL / ChangeNetConfigSec() 
# 3) Shortcut on desktop creation / createShortCut()
# 4) Show Windows Desktop
# 5) no reporting.

from sikuli import *
# import os
# import sys
# import time
# import shutil
# import unittest
# reload(unittest)
# import xmlrunner 

####### VAR #######
Settings.MoveMouseDelay = 0.0
myCommand = ""
### for Connect to Workplace windows ###
# Destination Name
VPNchar = "VPN Connection - "
VPNServerDestinationName = VPNchar + "MyCompany"
# Internet Address field
VPNServerInternetAddress = "MyCompany.com"
VPNUsername = "VPNUserPassword"

# if you want to prompt the user to change the VAR
# VPNServerInternetAddress = input("Please type the VPN address : ", VPNServerInternetAddress)
# VPNUsername = input("Please type the VPN User's Password : ", VPNUsername)


def RunBoxCall(myCommand):
    pressWinKey("r")    
    print"Win+R key activated"
    type(Key.CTRL + "a")
    type(Key.BACKSPACE)
    
    if myCommand is not "":
        type(myCommand)
        type(Key.ENTER)
        print("myCommand Activated")
    elif myCommand == "":
        print("The command is empty")
        
def makeWindowSizeMax(iconON, iconOFF):
#def makeNetConfigWindowMax(iconON, iconOFF):
    if exists(iconON):
        click(iconON)
        if exists("ta.png"): 
            click("ta.png")
        else:
            type(Key.ESC)
            return("Windows already max size.")

    elif exists(iconOFF):
        return("already resized and on the background")    


def SetUpNetConfig():
    RunBoxCall("control /name Microsoft.NetworkAndSharingCenter")
    sleep(1)
    nasc = switchApp("Network and Sharing Center")
    if nasc.hasWindow():
        nasc.focus()
    makeWindowSizeMax("1491380309351.png", "1491527284344.png")    
    click(Pattern("1491381493692.png").similar(0.74))
    click("1491381537678.png")
    type(Key.TAB + Key.ENTER)
    click("1491381623878.png")
    type(Key.TAB + Key.ENTER)
    print("Connect to Workplace Windows OK")

    click("1491382052626.png")
    sleep(1) 
    if exists("1491526563056.png"):
        click("1491526563056.png")       
        
    type(VPNServerInternetAddress)
    type(Key.TAB + VPNServerDestinationName)
    type(Key.TAB*4 + Key.ENTER)
    sleep(1)
    type(Key.ESC)
           

def ChangeNetConfigSec():
    RunBoxCall("control ncpa.cpl")
    makeWindowSizeMax("1491540308368.png","1491527284344.png")
    if exists("1491528880239.png"):
        rightClick("1491528880239.png")
        click("VPNProperties.png")
        click("1491529404470.png")
        if exists("1491529473536.png"): 
            click("1491529473536.png")
            click(Pattern("Security-PPtP.png").targetOffset(-16,-4))
        type(Key.TAB*2 + Key.ENTER)
        print("Parameters set-up Done!")


def createShortCut():
    RunBoxCall("control ncpa.cpl")
    makeWindowSizeMax("1491540308368.png","1491527284344.png")
    if exists("1491528880239.png"):
        rightClick("1491528880239.png")
        click("CreateShortcut.png")
        if exists("1491530256440.png"):
            #click to OK
            click(Pattern("1491530256440.png").targetOffset(71,26))
        
        
def pressWinKey(myKeyPressed):
    # Will press the Win Key + key of your choice 
    # example e.g pressWinKey("r") for Run box  
    keyDown(Key.WIN)
    keyDown(myKeyPressed)
    keyUp(myKeyPressed)
    keyUp(Key.WIN)    

def isShortcutOnDesktop(scutName = VPNServerDestinationName):
    " FUNCTION DOESN'T WORK. CAN'T PASS QUOTE INTO WIN "
    sleep(2)
    udpath = "%userprofile%/desktop/"    
    pressWinKey("r")
    type("cmd" + Key.ENTER)
    #print("The icon cannot be found on Windows Desktop.")
    #type("if exist " + udpath + " " + scutName + ".lnk echo "\"VPN OK!\"")
    #if exist("__CLICK-TO-CAPTURE__") == 2:
    #    print("VPN shortcut created on user's Desktop!")       
    sleep(5)

# Main - Running The Program
# Windows Size Max for Network and Sharing center
SetUpNetConfig()
print("The initial configuration has been set-up.")
print("Next, we are configuring parameters details. Work in progress")
ChangeNetConfigSec()
createShortCut()
#show Desktop.
pressWinKey("d")                
#isShortcutOnDesktop(VPNServerDestinationName)
sleep(5)
