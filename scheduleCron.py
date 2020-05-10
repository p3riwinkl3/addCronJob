import sys,argparse
from crontab import CronTab

my_cron = CronTab(user='raleineann.asis')

def addCronJob():
    job = my_cron.new(command='$(which python3) /home/raleineann.asis/automation/writeDate.py',comment='date info')
    job.minute.every(1)
    my_cron.write()

def removeCronJob():
    for job in my_cron:
        if job.comment == 'date info':
            my_cron.remove(job)
            my_cron.write()

def view():
    for job in my_cron:
        print(job)

# action = sys.argv[1]
parser = argparse.ArgumentParser()
parser.add_argument('-action','--action',action='store',dest='action', choices=['add','remove','view'],default='view')
args = parser.parse_args()
action = args.action
print(action)
# for job in my_cron:
#     print(job)

