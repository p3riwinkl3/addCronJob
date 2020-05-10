import datetime

with open('/home/raleineann.asis/automation/dateInfo.txt','a') as outFile:
    outFile.write('\n' + str(datetime.datetime.now()))