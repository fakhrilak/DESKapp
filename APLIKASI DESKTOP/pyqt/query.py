import subprocess
import json
import time
 
# traverse the info
def query_system():
    Id = subprocess.check_output(['systeminfo']).decode('utf-8').split('\n')
    value=[]
    for item in Id:
        value.append(item)

    print(value[33])
    types = []
    values=[]
    petik = []
    # arrange the string into clear info
    for item in value:
        if len(item) > 2:
            panjang = ""
            for i in item:
                panjang = panjang + i
                if i == ":" :
                    petik.append(len(panjang))

    count = 0            
    for item in Id:
        if len(item) > 2:
            types.append(item[:26])
            values.append(item[26:len(item)])
            count += 1
    return types,values