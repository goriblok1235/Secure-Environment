# Import module
import wmi
import os
import time

# Initializing the wmi constructor
f = wmi.WMI()

flag = 0

# Iterating through all the running processes
# while True:
def checking():
 for process in f.Win32_Process():
    if "notepad.exe" == process.Name:
	    # print("Application is Running")
        password = input("Enter the pass:")
        if password=="Sudip":
            for process in f.Win32_Process():
               if "notepad.exe" != process.Name:
                   break
               else:
                   pass   
        else:
            os.system("TASKKILL /F /IM notepad.exe")
            time.sleep(10)
	    

if __name__=='__main__':
    while True:
        checking()   

