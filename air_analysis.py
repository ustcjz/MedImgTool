# -*- coding: utf-8 -*-  

import csv
import matplotlib.pyplot as plt
from matplotlib.ticker import MultipleLocator, FormatStrFormatter

def decade_trend():
	csv_file = file('./air.csv', 'r')
	fin = csv.reader(csv_file)
	lines = [ [line[0].split('/')[-1], line[10].strip()] for line in fin]

	decades_list = [ i for i in range(1900, 2010, 10)]
	group_labels = [ str(i)+'~'+str(i+10) for i in range(1900, 2010, 10) ]
	num_list = [ 0 for i in range(1900, 2010, 10)]

	for i in range(1, len(lines)):
		if lines[i][1]:
			year = (int(lines[i][0]) - 1900) / 10
			num_list[ year ] += int(lines[i][1])

	xmajorLocator   = MultipleLocator(10) #将x主刻度标签设置为20的倍数
	ax = plt.subplot(111) #注意:一般都在ax中设置,不再plot中设置
	ax.xaxis.set_major_locator(xmajorLocator)

	fata_trend = plt.plot(decades_list, num_list, '--r*')
	plt.xlabel('years(decodes)')
	plt.ylabel('fatalities num')
	plt.grid()
	plt.xticks(decades_list, group_labels, rotation=0) # replacing nums with pre-defined labels
	plt.title('fatalities trend')
	plt.legend(fata_trend, ('fatalities',), loc='upper left') # add legend
	plt.show()

if __name__ == '__main__':
	decade_trend()