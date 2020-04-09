"""
Cho số nguyên n,
Nếu n lẻ, print XAM
Nếu n chẵn và nằm trong đoạn từ 2 đến 5, print KO XAM
Nếu n chẵn và nằm trong đoạn từ 6 đến 20,print XAM
Nếu n chẵn và lớn hơn 20, prin XAM
VD:
Input 0
3 
Output 0
XAM 
"""

#!/bin/python3

import math
import os
import random
import re
import sys

if __name__ == '__main__':
    n = int(input().strip())