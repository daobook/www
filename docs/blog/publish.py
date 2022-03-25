import os
import sys
import shutil
import datetime

now = datetime.datetime.now()
month = now.strftime('%b').lower()
dir = f"{now.year}/{month}/{now.day}/"

os.system(f'mkdir -p {dir}')
shutil.copy(sys.argv[1], dir)
