#!/usr/bin/env python3

"""Main."""

import sys
from cpu import *

files = sys.argv[1]

if len(sys.argv) != 2:
    print('Error With File Name') 
else:
    cpu = CPU()
    cpu.load(files)
    cpu.run()

