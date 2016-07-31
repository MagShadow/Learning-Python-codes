# test zip
import os
import time

source=['zipcontent\\','C:\\ziptest\\']
target_dir='ziptarget\\'
today=target_dir+time.strftime("%Y%m%d")
now=time.strftime("%H%M%S")
comment=input("Write a comment:")

if not os.path.exists(today): os.mkdir(today)
target=today+os.sep+now+'_'+comment.replace(' ','_')+'.rar'
#print(target)
#rar_command="WinRAR a -r -ep1 {0} {1}".format(target,source[0])
for i in source:
    rar_command="WinRAR a -r -ep1 {0} {1}".format(target,i)
    if os.system(rar_command)!=0:
        print("Error!")
