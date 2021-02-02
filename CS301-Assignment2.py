#Assignment 2 - CS301
#Created by Cody Cox

import time

def bench(f,inp):
    t1 = time.time()
    ans = f(inp)
    t2 = time.time()
    t = t2-t1
    return t

#ToDo:
#copy portions of lists mylist[:20k], mylist[:40k], mylist[:60k], ...
#rather than using multiple data files, that way only 1 somewhat large data file is needed

#run smaller iterations to extract more results - as shown in class, iterations of 10k up to 200k seem good

listData1k = list(open('data1k.txt').read().split())
listData10k = list(open('data10k.txt').read().split())
listData100k = list(open('data100k.txt').read().split())
listData1m = list(open('data1m.txt').read().split())
listData10m = list(open('data10m.txt').read().split())
listData100m = list(open('data100m.txt').read().split())

dictData1k = {}
dictData10k = {}
dictData100k = {}
dictData1m = {}
dictData10m = {}
dictData100m = {}
for line in listData1k:
    if line not in dictData1k:
        dictData1k[line] = 1
for line in listData10k:
    if line not in dictData10k:
        dictData10k[line] = 1
for line in listData100k:
    if line not in dictData100k:
        dictData100k[line] = 1
for line in listData1m:
    if line not in dictData1m:
        dictData1m[line] = 1
for line in listData10m:
    if line not in dictData10m:
        dictData10m[line] = 1
for line in listData100m:
    if line not in dictData100m:
        dictData100m[line] = 1

#List operations: (List is a collection which is ordered and changeable. Allows duplicate members)
#append
#remove
#look 'in'

#Dictionary operations: (Dictionary is a collection which is unordered and changeable. No duplicate members)
#add key, value
#remove key, value
#look 'in'

#This function converts the data 1k, 10k, and 100k to a list using the list() method
#1k bench: 0.0
#10k bench: 0.0010
#100k bench: 0.0120
#1m bench: 0.1640
#10m bench: 1.5295
#100m bench: 15.6375
def listBuild(data): #appears to be linear - O(n)
    listData = list(open(data).read().split())

#This function appends a number to lists of different sizes - NOTE: running this on the same list more than once runs significantly faster
    #I.e: 100m bench 2nd time: 0.0
#1k bench: 0.0
#10k bench: 0.0
#100k bench: 0.0                                         
#1m bench: 0.01701831817626953
#10m bench: 0.1470329761505127
#100m bench: 1.369307518005371
def listAppend(data): #appears to be linear - O(n)
    data.append(651612395876)

#This function inserts an element at the end of lists of different sizes - NOTE: running this on the same list more than once runs significantly faster
    #I.e: 100m bench 2nd time: 0.0
#1k bench: 0.0
#10k bench: 0.0
#100k bench: 0.0
#1m bench: 0.013002634048461914
#10m bench: 0.130936861038208
#100m bench: 1.0292210578918457
def listInsertLast(data): #appears to be linear - O(n)
    data.insert(-1, 651612395876)

#This function inserts an element at the beginning of lists of different sizes - NOTE: Running this on the same list more than onces runs significantly faster
    #I.e: 100m bench 2nd time: 0.10252714157104492
#1k bench: 0.0
#10k bench: 0.0
#100k bench: 0.002984762191772461
#1m bench: 0.01401519775390625
#10m bench: 0.1440427303314209
#100m bench: 0.99920654296875
def listInsertFirst(data): #appears to be linear - O(n)
    data.insert(0, 651612395876)

#This function inserts an element in the middle of lists of different sizes - NOTE: Running this on the same list more than onces runs significantly faster
    #I.e: 100m bench 2nd time: 0.05102252960205078
#1k bench: 0.0
#10k bench: 0.0
#100k bench: 0.0
#1m bench: 0.015014171600341797
#10m bench: 0.1390514373779297
#100m bench: 0.8201754093170166
def listInsertMiddle(data): #appears to be linear - O(n)
    middle = int(len(data) / 2)
    data.insert(middle, 651612395876)

#This function removes the last element from lists of different sizes - NOTE: Running this on the same list more than onces runs significantly faster
    #I.e: 100m bench 2nd time: 1.475334882736206
#1k bench: 0.0
#10k bench: 0.0
#100k bench: 0.010002374649047852
#1m bench: 0.10202312469482422
#10m bench: 1.1307294368743896
#100m bench: 8.091892004013062
def listRemoveLast(data): #appears to be linear - O(n)
    data.remove(data[-1])

#This function removes the first element from lists of different sizes - NOTE: Running this on the same list more than onces runs significantly faster
    #I.e: 100m bench 2nd time: 0.08701968193054199
#1k bench: 0.0
#10k bench: 0.0
#100k bench: 0.0020117759704589844
#1m bench: 0.0170137882232666
#10m bench: 0.19404387474060059
#100m bench: 1.1422569751739502
def listRemoveFirst(data): #appears to be linear - O(n)
    data.remove(data[1])

#This function removes the middle element from lists of different sizes - NOTE: Running this on the same list more than onces runs significantly faster
    #I.e: 100m bench 2nd time: 0.7801940441131592
#1k bench: 0.0
#10k bench: 0.0
#100k bench: 0.006014585494995117
#1m bench: 0.06602835655212402
#10m bench: 0.656470775604248
#100m bench: 2.717622756958008
def listRemoveMiddle(data): #appears to be linear - O(n)
    middle = int(len(data) / 2)
    data.remove(data[middle])

#This function searches for the last element in lists of different sizes - NOTE: Running this on the same list more than onces runs significantly faster
    #I.e: 100m bench 2nd time: 1.5620203018188477
#1k bench: 0.0
#10k bench: 0.0010139942169189453
#100k bench: 0.011002540588378906
#1m bench: 0.11146259307861328
#10m bench: 1.139247179031372
#100m bench: 4.848093032836914
def listSearch(data): #appears to be linear - O(n)
    if data[-1] in data:
        return True
    else:
        return False

#This function adds a key and value to dictionaries of different sizes
#1k bench: 0.0
#10k bench: 0.0
#100k bench: 0.0
#1m bench: 0.0
#10m bench: 0.0
#100m bench: 0.0
def dictAppend(data): #adding a key and value to a dictionary appears to be constant
    data[651612395876] = 1

#This function tries to remove a key from dictionaries of different sizes
#1k bench: 0.0
#10k bench: 0.0
#100k bench: 0.0
#1m bench: 0.0
#10m bench: 0.0
#100m bench: 0.0
def dictRemove(data): #removing a key from a dictionary appears to be constant
    data.pop(651612395876, None)

#This function searches for a key in dictionaries of different sizes - should be run after dictAppend
#1k bench: 0.0
#10k bench: 0.0
#100k bench: 0.0
#1m bench: 0.0
#10m bench: 0.0
#100m bench: 0.0
def dictSearch(data): #in operator for searching dictionaries appear to be constant
    if 651612395876 in data:
        return True
    else:
        return False
