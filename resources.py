#-------------------------------------------------------------------------------
# Name:        resources
# Purpose:
#
# Author:      ObsidianFire99
#
# Created:     09/03/2013
# Copyright:   (c) ObsidianFire99 2013
# Licence:     Creative Commons Attribution Unported 3.0
#-------------------------------------------------------------------------------
import math

def splitdig(num):
    innum = num
    power = 10**len(str(innum))
    power = power / 10
    numlist = []
    while not power == 0:
        numlist.append(int(math.floor(innum / power)))
        innum = innum % power
        power = power / 10
    return numlist[:]
