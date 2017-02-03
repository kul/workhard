import sys
import random
import time

if len(sys.argv) > 1:
    fname = sys.argv[1]
else:
    fname = 'build.log'

with open(fname) as f:
    lines = f.readlines()

n = len(lines)
i = 0
while True:
    print lines[i],
    i = (i+1) % n
    time.sleep(random.uniform(0,.5))
