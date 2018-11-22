import os
from datetime import datetime as dt
import time

#примеры с переводо времени в дату и обратно
#http://kamedov.ru/preobrazovanie-daty-v-python-iz-datetime-v-time/

files = 'files'
current_dir = os.path.dirname(os.path.abspath(__file__))
folder_files_way = os.path.join(current_dir, files)
files_list = os.listdir(folder_files_way)

print(current_dir)
print(folder_files_way)
print(files_list)
for file in files_list:
    temp = os.path.join(folder_files_way, file)
    timestamp = os.stat(temp).st_ctime
    print('--------------------------------')
    print(temp)
    print(os.stat(temp))
    print(timestamp)
    # print(date(os.stat(temp).st_ctime))
    print(dt.fromtimestamp(os.stat(temp).st_ctime).strftime("%Y %m, %d"))
    print('--------------------------------')
    dt_obj = dt.fromtimestamp(timestamp)
    print(dt_obj)
    print(repr(dt_obj))
    print('--------------------------------')
    time_tuple = time.gmtime(timestamp)
    print(time_tuple)
    print(repr(time_tuple))
    print('--------------------------------')
    with open(os.path.join(folder_files_way, file), encoding='utf8') as info:
        # print(info.read())
        text = info.read()
        # print(text)
