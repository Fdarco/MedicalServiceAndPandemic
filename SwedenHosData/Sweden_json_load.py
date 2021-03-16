# -*- coding='utf-8' -*-

import json
import csv
from datetime import datetime

f = 'Sweden_intensive.json'
# f = 'Sweden_cumulative_intensive.json'
fc = open(f)
Sdata = json.load(fc)
outdata = []
# print(Sdata['features'])
udata = Sdata['features']
outdata = []

for i in range(len(udata)):
    # print(udata[i])
    intensive_data = udata[i]['attributes']['Antal_intensivvardade']
    # intensive_data = udata[i]['attributes']['Kumulativa_intensivvardade']
    dtime = datetime.fromtimestamp(udata[i]['attributes']['Statistikdatum']/1000)
    str_dtime = datetime.strftime(dtime, '%Y-%m-%d')
    outdata.append([str_dtime, dtime, intensive_data])
    
# with open('Sweden_intensive_cumul_data.csv', 'w', newline='') as csvfile:
with open('Sweden_intensive_daily_data.csv', 'w', newline='') as csvfile:
    writer = csv.writer(csvfile, delimiter=',')
    writer.writerow(['date', 'intensive daily'])
    # writer.writerow(['date', 'intensive cumulative'])
    for i in range(len(outdata)):
        writer.writerow([outdata[i][0], outdata[i][2]])
    