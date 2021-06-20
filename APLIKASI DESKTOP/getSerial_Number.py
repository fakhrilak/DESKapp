import os
import sys

serial_number = os.popen("wmic baseboard get serialnumber")
A = []
for i in serial_number:
    A.append(i)

print(A)