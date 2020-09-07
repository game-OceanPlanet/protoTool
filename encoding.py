# -*- coding:utf-8 -*- 
import sys, codecs

coding = 'UTF-8'
def __init__():
    if sys.stdout.encoding != coding:
        sys.stdout = codecs.getwriter(coding)(sys.stdout.buffer, 'strict')
    if sys.stderr.encoding != coding:
        sys.stderr = codecs.getwriter(coding)(sys.stderr.buffer, 'strict')
        
__init__()
def log(s):
    print(s)
