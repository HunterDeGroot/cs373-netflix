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

from Netflix import netflix_solve

# -----------
# TestCollatz
# -----------

class TestNetflix (TestCase) :
    # ----
#     read
#     ----
# 
#     def test_read (self) :
#         s    = "1 10\n"
#         i, j = collatz_read(s)
#         self.assertEqual(i,  1)
#         self.assertEqual(j, 10)
# 
#     ----
#     eval
#     ----
# 
#     def test_eval_1 (self) :
#         v = collatz_eval(9, 9)
#         self.assertEqual(v, 20)
# 
#     def test_eval_2 (self) :
#         v = collatz_eval(100000, 200)
#         self.assertEqual(v, 351)
# 
#     def test_eval_3 (self) :
#         v = collatz_eval(210, 201)
#         self.assertEqual(v, 89)
# 
#     def test_eval_4 (self) :
#         v = collatz_eval(900, 1000)
#         self.assertEqual(v, 174)
#         
#     ----
#     cycles
#     ----    
#     
#     def test_eval_5 (self) :
#         v = collatz_cycles(1)
#         self.assertEqual(v, 1)
# 
#     def test_eval_6 (self) :
#         v = collatz_cycles(5)
#         self.assertEqual(v, 6)
# 
#     def test_eval_7 (self) :
#         v = collatz_cycles(10)
#         self.assertEqual(v, 7)
# 
#     def test_eval_8 (self) :
#         v = collatz_cycles(11)
#         self.assertEqual(v, 15)
# 
#     -----
#     print
#     -----
# 
#     def test_print (self) :
#         w = StringIO()
#         collatz_print(w, 1, 10, 20)
#         self.assertEqual(w.getvalue(), "1 10 20\n")

    # -----
    # solve
    # -----

    def test_solve (self) :
        collatz_solve()
        self.assertEqual(0, 0)

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
