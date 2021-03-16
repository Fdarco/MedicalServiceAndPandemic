# -*- coding='utf-8' -*-

from matplotlib import pyplot as plt
import seaborn as sns
import pandas as pd
import csv

output_data = []
with open('violin_chart3.csv', 'r') as csvfile:
	next(csvfile)
	lines = csv.reader(csvfile)
	for line in lines:
		parameter = line[0]
		China_data = float(line[1])
		US_data = float(line[2])
		Sweden_data = float(line[3])
		output_data.append([parameter, 'China', China_data])
		output_data.append([parameter, 'US', US_data])
		output_data.append([parameter, 'Sweden', Sweden_data])

with open('format_data.csv', 'w', newline='') as f:
	writer = csv.writer(f, delimiter=',')
	writer.writerow(['Parameters', 'Countries', 'Values'])
	for i in range(len(output_data)):
		writer.writerow(output_data[i])

df = pd.read_csv('format_data.csv')
print(df.head)
sns.set_style('white')
ax = sns.violinplot(x='Parameters', y='Values', hue='Countries', inner='box', cut=2, data=df, palette='Pastel1')
sns.despine()
# plt.legend(loc=2)
plt.rcParams['ytick.direction'] = 'in'
plt.show()




