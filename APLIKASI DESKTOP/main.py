from tkinter import *
import platform
import psutil
import requests
from data import data_system
from Table import Table
import wmi
 
c = wmi.WMI()   
my_system = c.Win32_ComputerSystem()[0]



root = Tk()
root.title("Spesifikasi laptop check")
canvas1 = Canvas(root,width=750,height=600) 
canvas1.pack()

data = platform.uname()
# serch = Entry(root, width=50, fg='blue',font=('Arial',10,'bold'))
# canvas1.create_window(250,100,window=serch)

# def getData():
#     v1 = serch.get()
#     print(v1,end=" ")
#     print(data.system)

# button_submit = Button(text="Cari",command=getData,width=30,fg="red",font=("bold"))
# canvas1.create_window(250,150,window=button_submit)
newdata = []
newdata.append(123456789)
newdata.append(my_system.Workgroup)
newdata.append(my_system.WakeUpType)
newdata.append(my_system.UserName)
newdata.append(my_system.TotalPhysicalMemory)
newdata.append(my_system.ThermalState)
newdata.append(my_system.SystemType)
newdata.append(my_system.SystemFamily)
newdata.append(my_system.Status)
newdata.append(my_system.Roles)
newdata.append(my_system.ResetLimit)
newdata.append(my_system.ResetCount)
newdata.append(my_system.ResetCapability)
newdata.append(my_system.PrimaryOwnerName)
newdata.append(my_system.PowerSupplyState)
newdata.append(my_system.PowerState)
newdata.append(my_system.PowerOnPasswordStatus)
newdata.append(my_system.PCSystemTypeEx)
newdata.append(my_system.PCSystemType)

Table(canvas1,data,500,100,60)
Table(canvas1,data_system,150,100,30)
Table(canvas1,newdata,500,221,60)

data3 = list(data) + newdata
dickku = {}

for i in range(21):
    dickku.update({data_system[i]:data3[i]})
dickku.update({'serial':"123344569"})
import json
fix_data = {
    "laptop":dickku,
    "user":{
        "serial": "12345666",
        "uid": "12345",
        "cn": "Fahril",
        "displayName": "Fahril",
        "sn": "Santoso",
        "givenName": "Jarwo",
        "personalTitle": "ST",
        "o": "PT STT",
        "ou": "IT Departement",
        "postalAddress": "12345",
        "postalCode": "54321",
        "c": "Indonesia"
    }
}
headers = {'API-KEY': 'blerg', 'Accept-Encoding': 'UTF-8', 'Content-Type': 'application/json'}

r = requests.post('http://111482feb5e7.ngrok.io/login',data=json.dumps(fix_data),headers=headers)

root.mainloop()