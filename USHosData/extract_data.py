# -*- coding='utf-8' -*-

import csv
import sqlite3
from datetime import datetime

def none_as_zero(input):
    if input != '':
        return int(input)
    else:
        return 0

extracted_data = [[], [], [], [], [], [], [], []]
with open('all-states-history.csv', 'r') as csvfile:
    next(csvfile)
    lines = csv.reader(csvfile)
    for line in lines:
        # date = datetime.strptime(line[0], '%Y-%m-%d')
        date = line[0]
        state = line[1]
        dataQuality = line[2]
        hospitalized = none_as_zero(line[7])
        hospitalized_cum = none_as_zero(line[8])
        hospitalized_cur = none_as_zero(line[9])
        hospitalized_inc = none_as_zero(line[10])
        inICUcumu = none_as_zero(line[11])
        inICUcurr = none_as_zero(line[12])
        
        if dataQuality in ['A', 'A+', 'B']:
            extracted_data[0].append(date)
            extracted_data[1].append(state)
            extracted_data[2].append(hospitalized)
            extracted_data[3].append(hospitalized_cum)
            extracted_data[4].append(hospitalized_cur)
            extracted_data[5].append(hospitalized_inc)
            extracted_data[6].append(inICUcumu)
            extracted_data[7].append(inICUcurr)
            
conn = sqlite3.connect('US_hospitalizations_inICU.db')
cur = conn.cursor()
cur.execute('''create table if not exists US_hos (
                udate timestamp,
                state text,
                hospitalized int,
                hospitalized_cum int,
                hospitalized_cur int,
                hospitalized_inc int,
                inICUcumu int,
                inICUcurr int);''')
conn.commit()

for i in range(len(extracted_data[0])):
    cur.execute('''insert into US_hos values (?, ?, ?, ?, ?, ?, ?, ?);''', (extracted_data[0][i], extracted_data[1][i], extracted_data[2][i], extracted_data[3][i], extracted_data[4][i], extracted_data[5][i], extracted_data[6][i], extracted_data[7][i]))
    
conn.commit()