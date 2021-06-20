import pymongo

myclient = pymongo.MongoClient("2.tcp.ngrok.io:10849")
mydb = myclient["test"]

def getAll_data(col):
    mycol = mydb[col]
    data=[]
    for x in mycol.find():
        data.append(x)
    return data