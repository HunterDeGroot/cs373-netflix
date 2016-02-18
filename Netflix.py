#!/usr/bin/env python3

# ---------------------------
# Netflix.py
# Copyright (C) 2015
# Hunter DeGroot
# ---------------------------

import os
import requests
import pickle

from urllib.request import urlopen


def netflix_solve () :
	if os.path.isfile('http://www.cs.utexas.edu/users/downing/public_html/netflix-caches/kh549-movie_average.pickle') :
		f = open('http://www.cs.utexas.edu/users/downing/public_html/netflix-caches/kh549-movie_average.pickle','rb')
		user_cache = pickle.load(f)
	else:
		# Read cache from HTTP
		bytes = urlopen('http://www.cs.utexas.edu/users/downing/netflix-caches/kh549-movie_average.pickle').read()
		user_cache = pickle.loads(bytes)
	print (user_cache[17747])

		
		# use user_cache here
