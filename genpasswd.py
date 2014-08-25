#!/usr/bin/python
import sys
import optparse
import getopt
from random import randrange

alpha = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z'];
ALPHA = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'];
special = ['!', '@', '#', '$', '%', '^', '&', '*', '(', ')', '[', ']', '{', '}', ';', ':', '"', ',', '?', '<', '>'];
NUMBERS = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0'];

def main():
    parser = optparse.OptionParser()
#    parser.add_option('-h', action="store", default=False)
    parser.add_option('-a', action="store_true", default=False, help="without lowercase alphabet")
    parser.add_option('-A', action="store_true", default=False, help="without uppercase alphabet")
    parser.add_option('-s', action="store_true", default=False, help="without special characteres")
    parser.add_option('-N', action="store_true", default=False, help="without numbers")
    parser.add_option('-n', action="store", dest="n", type="int", help="define the password size, default is 8")
    option, args = parser.parse_args(sys.argv[1:])
    passMap = [];
    passSize= 8;
    password = ""

    if not option.a:
        passMap = passMap + alpha
    if not option.A:
        passMap = passMap + ALPHA
    if not option.s:
        passMap = passMap + special
    if not option.N:
        passMap = passMap + NUMBERS
    if option.n is not None:
        passSize = option.n
    if len(passMap):
        for i in range (0, passSize):
            password = password + passMap[randrange(len(passMap))]
    print password


if __name__ == "__main__":
    main()
