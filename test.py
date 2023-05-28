from alive_progress import alive_bar
import time

total = 100
with alive_bar(total, manual=True) as bar:	# total 可以不指定，這時候只有百分比
    bar(0.5) # 進度到 50%
    time.sleep(0.5)
    bar(0.1) # 進度到 10% 
    time.sleep(0.5)
    bar(0.75) # 進度到 75%
    time.sleep(0.5)
    bar(1.0) # 進度到 100%
    time.sleep(0.5)
    bar(10) # 進度到 1000%
    for i in range(1,101):
        bar(i/100) # 設定進度為 i%
        time.sleep(0.05)