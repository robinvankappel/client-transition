# Backtracking based Python3 program to prall
import numpy as np
import time
import settings

def get_time(t):
    """
    Time difference between now and t
    """
    time_diff = round(time.time() - t,5)
    settings.time0 = time.time()
    return time_diff