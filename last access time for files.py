import datetime
import os
p=r"C:\\python34"
for f in os.listdir(p):
     if os.path.isfile(f) and f.endswith('txt'):
          print(f,'the last access is ',datetime.datetime.fromtimestamp(os.path.getatime(f)))
