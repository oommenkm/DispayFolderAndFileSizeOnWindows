"""
#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:     To display the Folder size and file size of a windows file system
#
# Author:      Oommen
#
# Created:     04/06/2011
# Copyright:   (c) Oommen 2011
# Licence:     This library is free software; you can redistribute it and/or modify
               it under the same terms as Python itself, either Python version 2.6 or,
               at your option, any later version of Python you may have available.
#-------------------------------------------------------------------------------
"""

#!/usr/bin/env python

import os

def getFolderSize(folder):
    total_size = os.path.getsize(folder)
    for item in os.listdir(folder):
        itempath = os.path.join(folder, item)
        if os.path.isfile(itempath):
            total_size += os.path.getsize(itempath)
        elif os.path.isdir(itempath):
            total_size += getFolderSize(itempath)
    return total_size

def main():
    absPath = raw_input('Absolute Path of the Folder : ') + '\\'
    dirList = os.listdir(absPath)

    dirListWithSize = []

    for itm in dirList:
        try:
            if os.path.isfile(absPath + itm):
                itmSize = os.path.getsize(absPath + itm) / 1024.0000 / 1024.0000 /1024.0000

            else:
                itmSize = getFolderSize(absPath + itm) / 1024.0000 / 1024.0000 /1024.0000
            dirListWithSize.append([itmSize, itm])
        except:
            pass
    dirListWithSize.sort()
    print "\n"
    for i in range(len(dirListWithSize) -1, -1, -1) :
        print dirListWithSize[i][1], ",", dirListWithSize[i][0], "G"
    pass

if __name__ == '__main__':
    main()
