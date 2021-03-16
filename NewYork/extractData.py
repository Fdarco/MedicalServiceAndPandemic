import datetime
import csv
import os

baseDir = 'US_data'

def get_data(file):
    with open(baseDir+'/'+file, 'r') as f:
        next(f)
        lines = csv.reader(f)
        for line in lines:
            countyName = line[0]
            if countyName == 'New York':
                Dtime = datetime.datetime.strptime(line[2], '%Y-%m-%d %H:%M:%S')
                Confirmed = int(line[5])
                Deaths = int(line[6])
                try:
                    Recovered = int(line[7])
                except:
                    Recovered = int(float(line[7]))
                try:
                    Active = int(line[8])
                except:
                    Active = int(float(line[8]))
                return [countyName, datetime.datetime.strftime(Dtime, '%Y/%m/%d')\
                        , Confirmed, Deaths, Recovered, Active]
            
outData = []
for file in os.listdir(baseDir):
    print(file)
    dData = get_data(file)
    outData.append(dData)
    
with open('NewYorkData.csv', 'w', newline='') as writefile:
    writer = csv.writer(writefile)
    writer.writerows(outData)