#!/bin/python3

import sys
from collections import Counter

if __name__ == "__main__":
#    s = input().strip()
    s = 'ccbbbaadeeee'

    common = sorted(Counter(s).items(), key=lambda e: (-e[1], e[0]))

    print(*[c+' '+str(n) for c,n in common[:3]], sep='\n')