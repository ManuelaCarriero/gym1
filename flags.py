# -*- coding: utf-8 -*-
"""
Created on Wed Jun 22 15:45:59 2022

@author: asus
"""

import argparse

import configparser



config = configparser.ConfigParser()



parser = argparse.ArgumentParser()



parser.add_argument("-square", help="display a square of a given number", type = float, metavar='value')

#parser.add_argument('integers', type=int, help='an integer for the accumulator')

parser.add_argument("-sqrt", help="display a square root of a given number", type=float)

parser.add_argument("-list", help="display a square root of a given number", nargs='+')

args = parser.parse_args()

if args.square:
    
    squaring = pow(args.square,2)
    
    print(squaring)

if args.sqrt:
    
    sqrt = args.sqrt**0.5
    
    print(sqrt)

if args.list:
    
    sqrt_lst = []
    
    for i in args.list:
        print(int(i))
        i = int(i)
        sqrt = i ** 0.5
        sqrt_lst.append(sqrt)
        
    print(sqrt_lst)
        
    
    print(args.list)
    
    print(args.list[0])

#print(squaring)  If you choose args.square it works when you lanch the program otherwise it gives an error because squaring is not defined.
"""
parser.add_argument('run', help='run Gillespie simulation')
parser.add_argument("filename", help="configuration file name")
parser.add_argument("-v", "--verbose", help="increase output verbosity", action="store_true")
parser.add_argument("-i","--increase", help="increase time limit", action="store_true")


args = parser.parse_args()
"""