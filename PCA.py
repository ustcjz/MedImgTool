#!/usr/bin/env python

import sys
import scipy.io as sio
import numpy as np
  
def USPS_PCA():  
	raw_data = sio.loadmat('./USPS.mat')
	A = raw_data['A']
	L = raw_data['L']

	meanMat = np.mean(A, axis=0) 
	newMat = A - meanMat 
	covMat = np.cov(newMat, rowvar=0)
      
	eigVals, eigVects = np.linalg.eig(np.mat(covMat)) # eigen value/vector 
	eigValIndice = np.argsort(eigVals) # sort

	eigNums = [10, 50, 100, 200]
	errArr = []
	reconImg = []
	for i, num in enumerate(eigNums):
		n_eigValIndice = eigValIndice[-1:-(num+1):-1]  # top n biggest eigVal indices
		n_eigVect = eigVects[:, n_eigValIndice]        

		lowDDataMat = newMat * n_eigVect               
		reconMat = (lowDDataMat * n_eigVect.T) + meanMat  # reconstruct

	    # calculate the error
		diffMat = A - reconMat
		currErr = sum([ sum([item*item for item in row]) for row in diffMat.tolist()])
		errArr.append(currErr)

		reconImg.append(reconMat[0])
		reconImg.append(reconMat[1])

	sio.savemat('./reconMat.mat', {'A':reconImg}) # save reconstruction mat
	print errArr

if __name__ == '__main__':
	USPS_PCA()