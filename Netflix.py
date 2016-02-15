#!/usr/bin/env python3

# ---------------------------
# Netflix.py
# Copyright (C) 2015
# Hunter DeGroot
# ---------------------------

import os
import requests

from urllib.request import urlopen


def netflix_solve () :
	if os.path.isfile('http://www.cs.utexas.edu/users/downing/public_html/netflix-caches/ad35988-movie_stddev_average.pickle') :
		f = open('http://www.cs.utexas.edu/users/downing/public_html/netflix-caches/ad35988-movie_stddev_average.pickle','rb')
		user_cache = pickle.load(f)
	else:
		# Read cache from HTTP
		bytes = urlopen('http://www.cs.utexas.edu/users/downing/netflix-caches/ad35988-movie_stddev_average.pickle').read()
		user_cache = pickle.loads(bytes)
		
		# use user_cache here