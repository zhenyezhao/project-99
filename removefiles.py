import os
import shutil
import time
def main ():
    path=input('enter the folder')
    days=30
    seconds=time.time()-(days*24*60*60)
    if os.path.exists(path):
        for i in os.walk(path):
            name,ext=os.path.splitext(i)
            ext=
