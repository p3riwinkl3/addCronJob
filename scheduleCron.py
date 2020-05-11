import sys,argparse, datetime
from crontab import CronTab

# Reference: https://stackabuse.com/scheduling-jobs-with-python-crontab/

my_cron = CronTab(user='raleineann')

def addCronJob():
    
    if jobtype == 'onetime':
        
        job = my_cron.new(command='$(which python3) /mnt/c/Users/raleineann.asis/Documents/PE-DevOps-Projects/python/cronJobAutomate/cronJobAutomate/writeDate.py',comment='date info')
        job.setall(datetime.datetime(2020, 5, 11, 13, 30))    
        my_cron.write()
        viewCronJob()
    if jobtype == 'recurring':
        pass

def removeCronJob():
    for job in my_cron:
        if job.comment == 'date info':
            my_cron.remove(job)
            my_cron.write()
    viewCronJob()

def viewCronJob():
    for job in my_cron:
        print(job)

# action = sys.argv[1]
parser = argparse.ArgumentParser()
parser.add_argument('-action','--action',action='store',dest='action', choices=['add','remove','view'],default='view')
parser.add_argument('-sdate','--start_date',action='store',dest='start_date',help="Date of the cronjob")
parser.add_argument('-chg_num','--change_number',action='store',dest='change_number',help="Change number")
parser.add_argument('-jobtype','--job_type',action='store',dest='job_type',help="One time or recurring")

args = parser.parse_args()
action = args.action
startdate = args.start_date

print(action)

viewCronJob()
# addCronJob()
# removeCronJob()



# for job in my_cron:
#     print(job)

