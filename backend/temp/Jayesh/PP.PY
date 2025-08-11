#!/bin/python3

import math
import os
import random
import re
import sys

def aVeryBigSum(ar):
    # Write your code here
    return sum(ar)


ar_count = int(input().strip())

ar = list(map(int, input().rstrip().split()))

result = aVeryBigSum(ar)