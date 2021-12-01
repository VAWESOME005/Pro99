import os
import shutil
import time

path = input('Enter the location that you want to organize: ')
days = int(input('What is the # of days a file can be (at the max): '))

seconds = time.time() - (days * 24 * 60 * 60)

 if os.path.exists(path):
     for root, dirs, files in os.walk(path):
         if seconds > os.stat(path).st_ctime:
             shutil.rmtree(path)



