import math
import os
import random
import re
import sys

# defined the function before it is called in the main function
def reverse_list(n, arr):
    if 1 <= n <= 1000 and 1 <= len(arr) <= 10000:
        re_arr = arr[::-1]
        return re_arr

# the main function in which input are convertd into a list and output are made
if __name__ == '__main__':
    n = int(input().strip())
    arr = list(map(int, input().rstrip().split()))
    
    re_arr = reverse_list(n, arr)
    re_arr_str = [str(x) for x in re_arr]
    output = " ".join(re_arr_str)
    print(output)
