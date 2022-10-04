import datetime
from math import floor,ceil
import sys

'''
00:01 - 09:00 25 USD

09:01 - 18:00 15 USD

18:01 - 00:00 20 USD

Saturday and Sunday

00:01 - 09:00 30 USD

09:01 - 18:00 20 USD

18:01 - 00:00 25 USD
'''
class worker:
    name=None
    work_time=None
    total_money=None

    dic_rules_workday={
        datetime.datetime.strptime("00:01", "%H:%M"):25,
        datetime.datetime.strptime("09:01", "%H:%M"):15,
        datetime.datetime.strptime("18:01", "%H:%M"):20,
    }

    dic_rules_weekend={
        datetime.datetime.strptime("00:01", "%H:%M"):30,
        datetime.datetime.strptime("09:01", "%H:%M"):20,
        datetime.datetime.strptime("18:01", "%H:%M"):25,
    }
    def __init__(self, line):
        sp=line.split("=")
        self.name = sp[0]
        self.work_time = sp[1].replace('\n','')

    def calc(self):
        orders=self.work_time.split(',')
        self.total_money=self.treat_order(orders)
        return self.total_money

    def obtain_time(self,code_time):
        weekday_start=code_time[:2]
        work_start=datetime.datetime.strptime(code_time[2:7], "%H:%M")
        work_end=datetime.datetime.strptime(code_time[8:], "%H:%M")
        return (weekday_start,work_start,work_end)

    def treat_order(self,code, money=0):
        if len(code)==0:
            return money
        pay=self.process_time(self.obtain_time(code[0]))
        money=money + pay
        return(self.treat_order(code[1:],money))

    def process_time(self,day):
        weekday_start,work_start,work_end =day
        worked_hours=ceil((work_end-work_start).total_seconds()/3600)
        dic_rules = self.dic_rules_weekend if (("SA" in weekday_start) | ("SU" in weekday_start)) else self.dic_rules_workday
        hour_pay =list(dic_rules[best]  for best in dic_rules if work_start>= best)[-1]
        return(worked_hours*hour_pay)

    def __str__(self):
        return("%s with work time %s and total money %s \n"%(self.name,self.work_time,self.total_money))

def get_workers(line):
    try:
        Worker=worker(line)
        Worker.calc()
        print(Worker)
    except:
        print("There was an error with line %s"%line)

    
if __name__ == '__main__':
    try:
        name=sys.argv[1]
    except(IndexError):
        print("Requires a file")
    else:
        with open(name) as f:
            lines=f.readlines()
        list(map(get_workers,lines))

