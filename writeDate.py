import datetime

with open('/home/raleineann/dateInfo.txt','a') as outFile:
    outFile.write('\n' + str(datetime.datetime.now()))