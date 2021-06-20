from PyQt5.QtWidgets import QApplication,QMainWindow,QFrame
from Table import TableView
from query import query_system
import sys,os

getSerial =  os.popen("wmic bios get serialnumber").read().replace("\n","").replace("	","").replace(" ","")

print(getSerial[12:len(getSerial)])

A , B = query_system()
A.insert(0,"Serial Number:")
B.insert(0," " + getSerial[12:len(getSerial)])
data = {'System': A,
        'value': B}

 
def main(args):
    app = QApplication(args)
    table = TableView(data, 56, 2)
    table.show()
    table.resize(500,500)
    sys.exit(app.exec_())
 
if __name__=="__main__":
    main(sys.argv)