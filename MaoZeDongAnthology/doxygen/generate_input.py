import os
from os.path import *

folder = dirname(abspath(__file__))
a = list(os.listdir(join(folder, "../src")))
a.sort()
b = ['SUMMARY.md']
for i in a:
    if i.startswith('SUMMARY') or i.startswith('目录'):
        continue
    b.append(f'../src/{i}')
print('\\\n'.join(b))
