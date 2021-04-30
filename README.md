Tests include 4 passes, 4 errors and 1 failure. Tests for input handlng assume that None is returned for invalid input.

Unittest Results: \
test_add (__main__.TestCalc) ... ok \
test_add_str (__main__.TestCalc) ... ERROR \
test_divide (__main__.TestCalc) ... ok \
test_divide_char (__main__.TestCalc) ... ERROR \
test_divide_zero (__main__.TestCalc) ... ERROR \
test_multiply (__main__.TestCalc) ... ok \
test_multiply_char (__main__.TestCalc) ... FAIL \
test_sub (__main__.TestCalc) ... ok \
test_sub_char (__main__.TestCalc) ... ERROR \

PyTest Results: \
FAILED test_calc_pytest.py::test_divide_zero - ZeroDivisionError: division by zero \
1 failed, 4 passed in 0.15s 