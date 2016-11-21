#!/usr/bin/env python

# --------------------------------------------------------
# Faster R-CNN
# Copyright (c) 2015 Microsoft
# Licensed under The MIT License [see LICENSE for details]
# Written by Ross Girshick
# --------------------------------------------------------

"""
Demo script showing detections in sample images.

See README.md for installation instructions before running.
"""

import sys

def valid_count(file):
	f = open(file)
	lines = f.readlines()
	count = 0
	for line in lines:
		line = line.strip()
		if not line:
			break

		items = line.split('   ')
		if len(items)<4:
			continue

		#print items[2]
		if float(items[2]) <= 4 or float(items[2]) >= 6:
			count += 1

	print 'valid count: ' + str(count)

def filter_valid(all_file, curr_file, save_file):
	all_f = open(all_file)
	lines = all_f.readlines()
	adict = {}
	for line in lines:
		line = line.strip()
		if not line:
			break

		items = line.split('   ')
		if len(items)<4:
			continue

		adict[items[0]] = float(items[2]) #  {name, score}


	curr_f = open(curr_file)
	save_f = open(save_file, 'w')
	lines = curr_f.readlines()
	count = 0
	scores = [0]*10
	for line in lines:
		line = line.strip()
		if not line:
			break

		items = line.split('.')
		name = items[0]
		#print name + '\t' + name[0:len(name)-1]
		name = name[0:len(name)-1]

		if adict.has_key(name):
			scores[int(adict[name])] += 1

		save_f.write(line +'\t'+str(adict[name])+'\n')

	save_f.close()

	print scores
	print sum(scores)
	print len(lines)
#	print 'number in [4, 6]: '+str(count)

if __name__ == '__main__':
	all_file = sys.argv[1]
	curr_file = sys.argv[2]
	save_file = sys.argv[3]

	filter_valid(all_file, curr_file, save_file)

	#valid_count(f)