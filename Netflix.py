#!/usr/bin/env python3

# ---------------------------
# Netflix.py
# Copyright (C) 2015
# Hunter DeGroot
# ---------------------------

import os
import requests
import pickle
import math
from numpy import mean, sqrt, square, subtract

from urllib.request import urlopen

movie_avgs     = None
cust_ratios    = None
correct_scores = None

def load_caches():
	global movie_avgs, cust_ratios, correct_scores

	if os.path.isfile('http://www.cs.utexas.edu/users/downing/public_html/netflix-caches/kdg445_movie_avgs.pickle') :
		f = open('http://www.cs.utexas.edu/users/downing/public_html/netflix-caches/kdg445_movie_avgs.pickle','rb')
		movie_avgs = pickle.load(f)
	else:
		# Read cache from HTTP
		bytes = urlopen('http://www.cs.utexas.edu/users/downing/netflix-caches/kdg445_movie_avgs.pickle').read()
		movie_avgs = pickle.loads(bytes)
		# cust ratios
	
	if os.path.isfile('http://www.cs.utexas.edu/users/downing/public_html/netflix-caches/trp676-customer_ratio.pickle') :
		f = open('http://www.cs.utexas.edu/users/downing/public_html/netflix-caches/trp676-customer_ratio.pickle','rb')
		cust_ratios = pickle.load(f)
	else:
		# Read ratios from HTTP
	               bytes = urlopen('http://www.cs.utexas.edu/users/downing/netflix-caches/trp676-customer_ratio.pickle').read()
	               cust_ratios = pickle.loads(bytes)
		# correct scores
	
	if os.path.isfile('http://www.cs.utexas.edu/users/downing/public_html/netflix-caches/mdg7227-real_scores.pickle') :
		f = open('http://www.cs.utexas.edu/users/downing/public_html/netflix-caches/mdg7227-real_scores.pickle','rb')
		correct_scores = pickle.load(f)
	else:
		# Read vals from HTTP
		bytes = urlopen('http://www.cs.utexas.edu/users/downing/netflix-caches/mdg7227-real_scores.pickle').read()
		correct_scores = pickle.loads(bytes)


def RMSE(a,p):
	return sqrt(mean(square(subtract(a,p))))
	

def netflix_solve (r, w) :
	global movie_avgs, cust_ratios, correct_scores	
	load_caches()

	# predict movie and compare with correct with RMSE
	movieId = 0
	error = 0
	ratingCount = 0
	for line in r :
		if ':' in line.strip() :
			movieId = line.split(':')[0]
			w.write(line)
		else :
			ratingCount += 1
			custId = line

			# better solution (cache is missing one value?!)
			prediction = movie_avgs[int(movieId)]

			try:
				prediction = movie_avgs[int(movieId)] * cust_ratios[int(custId)]
			except Exception:
				break

			w.write('%.2f' % prediction+"\n")			
			actual = 1

			try:
				actual = correct_scores[int(movieId)][int(custId)]
			except Exception:
				#print("Cust: " + str(custId))
				#print("Movie: " + str(movieId))
				break

			error += (actual - prediction)**2
			
	#w.write('RMSE: ' + '%.2f' % math.sqrt(error/ratingCount)+"\n")			 				
