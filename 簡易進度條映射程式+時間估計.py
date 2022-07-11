import threading
import time
import random

def progressbar(progress,total,title):
  tags = ['—','\\','|','/']
  tags1 = ['▏','▎','▍','▌','▋','▊','▉','█']
  tags2 = ['▁','▂','▃','▄','▅','▆','▇','█']
  t2 = time.time()
  seconds = t2-t1
  minute1 = int(seconds /60)
  second1 = int(seconds %60)
  if(progress>=0):
    seconds = ((t2-t1)/((progress+0.0000001)/total))-(t2-t1)
  else:
    seconds = 0
  minute2 = int(seconds /60)
  second2 = int(seconds %60)
  speed1 = 1/(t4-t3+0.00001)
  speed2 = 1/(t2-t4+0.00001)
  if(speed1 > speed2):
    speed1 = speed2
  if(t4!=t3):
    if(progress==0):
      print('{} |{:^50}| [{:^1}] {:^3} {}/{} [{:0<5}%] [{:>2}:{:>2} < {:>2}:{:>2},{:0<5}it/s]    '.format(title," "*int(50*(1-(progress)/total)),tags[progress%4],tags2[random.randint(0,7)]+tags2[random.randint(0,7)]+tags2[random.randint(0,7)]," "*(len(str(total))-len(str(progress)))+str(progress),total,round((100*(progress)/total),2),minute1,second1,"0","0",round(1/speed1,2)),end="\r")
    elif(progress==total):
      print('{} |{:^50}| [{:^1}] {:^3} {}/{} [{:0<5}%] [{:>2}:{:>2} < {:>2}:{:>2},{:0<5}it/s]    '.format(title,(tags1[7]*(int)(50*(progress)/total)),tags[progress%4],tags2[random.randint(0,7)]+tags2[random.randint(0,7)]+tags2[random.randint(0,7)]," "*(len(str(total))-len(str(progress)))+str(progress),total,round((100*(progress)/total),2),minute1,second1,"0","0",round(total/(t2-t1),2)),end="\r")
    elif(((progress)/total)<0):
      print('{} |{:^50}| [{:^1}] {:^3} {}/{} [{:0<5}%] [{:>2}:{:>2} < {:>2}:{:>2},{:0<5}it/s]    '.format(title,('⚠'+(" "*49)),tags[progress%4],tags2[random.randint(0,7)]+tags2[random.randint(0,7)]+tags2[random.randint(0,7)]," "*(len(str(total))-len(str(progress)))+str(progress),total,round((100*(progress)/total),2),minute1,second1,minute2,second2,round(1/speed1,2)),end="\r")
    elif(((progress)/total)>1):
      print('{} |{:^50}| [{:^1}] {:^3} {}/{} [{:0<5}%] [{:>2}:{:>2} < {:>2}:{:>2},{:0<5}it/s]    '.format(title,(tags1[7]*(int)(50*(progress)/total))+tags1[int((progress+0.00001)/total*400%8)]+'⚠',tags[progress%4],tags2[random.randint(0,7)]+tags2[random.randint(0,7)]+tags2[random.randint(0,7)]," "*(len(str(total))-len(str(progress)))+str(progress),total,round((100*(progress)/total),2),minute1,second1,"??","??",round(speed1,2)),end="\r")
    elif(1/(t4-t3)<1):
      print('{} |{:^50}| [{:^1}] {:^3} {}/{} [{:0<5}%] [{:>2}:{:>2} < {:>2}:{:>2},{:0<5}it/s]    '.format(title,(tags1[7]*(int)(50*(progress)/total))+tags1[int((progress+0.00001)/total*400%8)]+'⚠'+(" "*(int(50*(1-(progress+0.00001)/total)-1))),tags[progress%4],tags2[random.randint(0,7)]+tags2[random.randint(0,7)]+tags2[random.randint(0,7)]," "*(len(str(total))-len(str(progress)))+str(progress),total,round((100*(progress)/total),2),minute1,second1,minute2,second2,round(speed1,2)),end="\r")
    else:
      print('{} |{:^50}| [{:^1}] {:^3} {}/{} [{:0<5}%] [{:>2}:{:>2} < {:>2}:{:>2},{:0<5}it/s]    '.format(title,(tags1[7]*(int)(50*(progress)/total))+tags1[int((progress+0.00001)/total*400%8)]+(" "*int(50*(1-(progress+0.00001)/total))),tags[progress%4],tags2[random.randint(0,7)]+tags2[random.randint(0,7)]+tags2[random.randint(0,7)]," "*(len(str(total))-len(str(progress)))+str(progress),total,round((100*(progress)/total),2),minute1,second1,minute2,second2,round(speed1,2)),end="\r")
  elif(t4==t3):
    if(progress==0):
      print('{} |{:^50}| [{:^1}] {:^3} {}/{} [{:0<5}%] [{:>2}:{:>2} < {:>2}:{:>2},{:>5}it/s]    '.format(title," "*int(50*(1-(progress)/total)),tags[progress%4],tags2[random.randint(0,7)]+tags2[random.randint(0,7)]+tags2[random.randint(0,7)]," "*(len(str(total))-len(str(progress)))+str(progress),total,round((100*(progress)/total),2),minute1,second1,"0","0","∞"),end="\r")
    elif(progress==total):
      print('{} |{:^50}| [{:^1}] {:^3} {}/{} [{:0<5}%] [{:>2}:{:>2} < {:>2}:{:>2},{:>5}it/s]    '.format(title,(tags1[7]*(int)(50*(progress)/total)),tags[progress%4],tags2[random.randint(0,7)]+tags2[random.randint(0,7)]+tags2[random.randint(0,7)]," "*(len(str(total))-len(str(progress)))+str(progress),total,round((100*(progress)/total),2),minute1,second1,"0","0",round(total/(t2-t1),2)),end="\r")
    elif(((progress)/total)<0):
      print('{} |{:^50}| [{:^1}] {:^3} {}/{} [{:0<5}%] [{:>2}:{:>2} < {:>2}:{:>2},{:>5}it/s]    '.format(title,('⚠'+(" "*49)),tags[progress%4],tags2[random.randint(0,7)]+tags2[random.randint(0,7)]+tags2[random.randint(0,7)]," "*(len(str(total))-len(str(progress)))+str(progress),total,round((100*(progress)/total),2),minute1,second1,minute2,second2,"∞"),end="\r")
    elif(((progress)/total)>1):
      print('{} |{:^50}| [{:^1}] {:^3} {}/{} [{:0<5}%] [{:>2}:{:>2} < {:>2}:{:>2},{:>5}it/s]    '.format(title,(tags1[7]*(int)(50*(progress)/total))+tags1[int((progress+0.00001)/total*400%8)]+'⚠',tags[progress%4],tags2[random.randint(0,7)]+tags2[random.randint(0,7)]+tags2[random.randint(0,7)]," "*(len(str(total))-len(str(progress)))+str(progress),total,round((100*(progress)/total),2),minute1,second1,"??","??","∞"),end="\r")
    else:
      print('{} |{:^50}| [{:^1}] {:^3} {}/{} [{:0<5}%] [{:>2}：{:>2}<{:>2}：{:>2},{:>5}it/s]    '.format(title,(tags1[7]*(int)(50*(progress)/total))+tags1[int((progress+0.00001)/total*400%8)]+(" "*int(50*(1-(progress+0.00001)/total))),tags[progress%4],tags2[random.randint(0,7)]+tags2[random.randint(0,7)]+tags2[random.randint(0,7)]," "*(len(str(total))-len(str(progress)))+str(progress),total,round((100*(progress)/total),2),minute1,second1,minute2,second2,"∞"),end="\r")

def main():
  global t4,t3,i
  for i in range(0,number+1):
    t4 = time.time()
    #time.sleep(0.2)
    time.sleep(random.uniform(0,1.5))
    con.acquire()
    progressbar(i,number,name)
    con.release()
    t3=t4
  print("\n---Finish---")
  con.acquire()

def refresh():
  global i,number,name
  while(1):
    time.sleep(0.1)
    con.acquire()
    progressbar(i,number,name)
    con.release()

t1 = time.time()
t2 = time.time()
t3 = time.time()
t4 = time.time()
number = 10000 #9223372036854775807
name = "Hello Neko" ; i=0
con = threading.Condition()
Thread1 = threading.Thread(target = main)
Thread2 = threading.Thread(target = refresh)
Thread2 .setDaemon(True)
Thread1 .start()
Thread2 .start()

