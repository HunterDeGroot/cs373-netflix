#!/usr/bin/env python3

# ------------------------------
# Copyright (C) 2015
# Hunter DeGroot
# ------------------------------

# -------
# imports
# -------

import sys

from Netflix import netflix_solve

# ----
# main
# ----

if __name__ == "__main__" :
    netflix_solve()

"""
% cat RunNetflix.in


% RunNetflix.py < RunNetflix.in > RunNetflix.out



% cat RunNetflix.out


% pydoc3 -w Netflix
# That creates the file Netflix.html
"""