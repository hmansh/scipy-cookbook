#!/usr/bin/env python3
import os
import sys
import subprocess

if sys.argv[1:2] == ['install']:
    subprocess.call(['git', 'fetch', '--unshallow'],
                    cwd=os.path.abspath(os.path.dirname(__file__)))
    subprocess.check_call([sys.executable, 'build.py'],
                          cwd=os.path.abspath(os.path.dirname(__file__)))
else:
    print("Usage: setup.py install\n\nThis will just run build.py --- useful for readthdocs.org\n")
    sys.exit(1)
