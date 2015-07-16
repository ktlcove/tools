#!/usr/bin/env python3
#
# create_date : 2015-07-16
# author : ktlcove
# mail : ktl_cove@126.com
#
# read an xls file to dictionary
# using: dirt = Xls_Dirt('path/to/file.xls',empty='')
# this return a dirt
# dirt = { 'sheet1name' : [ ['a1','a2'...] , ['b1','b2'...]...],
#          'sheet2name' : [...],
#	   ...}
# if a position is empty replace it with empty's value
# line cmd ./read_xls.py file.xls
# print all in file.xls

import xlrd

class Xls_Dirt():

    def __init__( self , xls_file , empty = ''):

        Book = xlrd.open_workbook(xls_file)
        DIRT = {}

        for sheet in Book.sheets():
            DIRT[sheet.name] = []
            for i in range(sheet.nrows):
                DIRT[sheet.name].append([])
                for j in sheet.row_values(i):
                    if j == '' : j = empty
                    DIRT[sheet.name][i].append(j)
        self.data = DIRT

    def show(self):
        for k in self.data.keys():
            for i in self.data[k]:
                for j in i:
                    print (j,end=' ')
                print()

if __name__ == '__main__':
    import sys
    try:
        a=Xls_Dirt(sys.argv[1],empty=sys.argv[2])
    except:
        try:
            a=Xls_Dirt(sys.argv[1])
        except:
            print ( 'argument error need a file name')
            sys.exit(1)
    a.show()
