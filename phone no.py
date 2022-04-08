#!/bin/python3

import math
import os
import random
import re
import sys

def getPhoneNumber(s):
    dic = {
    'zero' : '0',
    'one': '1',
    'two': '2',
    'three': '3',
    'four': '4',
    'five': '5',
    'six': '6',
    'seven': '7',
    'eight': '8',
    'nine': '9',
    'double':'10',
    'triple':'11',
    }
    
    temp=""
    d=0
    t=0
    for ele in s.split(" "):
        if dic[ele]=='10':
            if d==1:
               pass 
            else:
                d+=1
                
        elif dic[ele]=='11':
            d+=2
        else:
            j=0
            while j<=d or j<=t:
                temp = temp+''.join(dic[ele])
                j+=1
            d=0
            t=0
        
    return temp
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = getPhoneNumber(s)

    fptr.write(result + '\n')

    fptr.close()
