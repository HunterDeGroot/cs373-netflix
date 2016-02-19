#!/usr/bin/env python3

# -------------------------------
# projects/collatz/TestCollatz.py
# Copyright (C) 2015
# Hunter DeGroot
# -------------------------------

# https://docs.python.org/3.4/reference/simple_stmts.html#grammar-token-assert_stmt

# -------
# imports
# -------

from io       import StringIO
from unittest import main, TestCase
import sys

from Netflix import netflix_solve

# -----------
# TestCollatz
# -----------

class TestNetflix (TestCase) :
   
    # -----
    # solve
    # -----

    def test_solve (self) :
    	s = StringIO("1000:\n98259\n79755\n1:\n30878\n317050")
    	w = StringIO()
    	test = netflix_solve(s, w)
    	self.assertEqual(w.getvalue(), "1000:\n3.5\n3.9\n1:\n3.8\n3.6\nRMSE: 1.16\n")

    def test_solve2 (self) :
    	s = StringIO("798:\n3381\n1000:\n98259\n79755")
    	w = StringIO()
    	test = netflix_solve(s, w)
    	self.assertEqual(w.getvalue(), "798:\n3.9\n1000:\n3.5\n3.9\nRMSE: 1.08\n")

    def test_solve3 (self) :
    	s = StringIO("10:\n1952305\n1531863\n1000:\n2326571\n977808")
    	w = StringIO()
    	test = netflix_solve(s, w)
    	self.assertEqual(w.getvalue(), "10:\n2.9\n2.9\n1000:\n3.4\n2.9\nRMSE: 0.21\n")

# ----
# main
# ----

if __name__ == "__main__" :
    main()

"""
% coverage3 run --branch TestCollatz.py >  TestCollatz.out 2>&1



% coverage3 report -m                   >> TestCollatz.out



% cat TestCollatz.out
.......
----------------------------------------------------------------------
Ran 7 tests in 0.001s

OK
Name          Stmts   Miss Branch BrMiss  Cover   Missing
---------------------------------------------------------
Collatz          18      0      6      0   100%
TestCollatz      33      1      2      1    94%   79
---------------------------------------------------------
TOTAL            51      1      8      1    97%
"""
