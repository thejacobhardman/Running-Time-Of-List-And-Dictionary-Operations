#Assignment 2 - CS301
#Outline Created by Cody Cox
#Finished by Jacob Hardman

import time

def bench(f,inp):
    t1 = time.time()
    ans = f(inp)
    t2 = time.time()
    t = t2-t1
    return t

listData1k = list(open('data1k.txt').read().split())
listData10k = list(open('data10k.txt').read().split())
listData100k = list(open('data100k.txt').read().split())
listData500k = list(open('data500k.txt').read().split())
listData1m = list(open('data1m.txt').read().split())

dictData1k = {}
dictData10k = {}
dictData100k = {}
dictData500k = {}
dictData1m = {}
for line in listData1k:
    if line not in dictData1k:
        dictData1k[line] = 1
for line in listData10k:
    if line not in dictData10k:
        dictData10k[line] = 1
for line in listData100k:
    if line not in dictData100k:
        dictData100k[line] = 1
for line in listData500k:
    if line not in dictData500k:
        dictData100k[line] = 1
for line in listData1m:
    if line not in dictData1m:
        dictData1m[line] = 1

listTimes = []
dictTimes = []

#List operations: (List is a collection which is ordered and changeable. Allows duplicate members)
#append
#remove
#look 'in'

#Dictionary operations: (Dictionary is a collection which is unordered and changeable. No duplicate members)
#add key, value
#remove key, value
#look 'in'

#This function converts the data 1k, 10k, and 100k to a list using the list() method
def listBuild(data): #appears to be linear - O(n)
    listData = list(open(data).read().split())

#This function appends a number to lists of different sizes
def listAppend(data): #appears to be linear - O(n)
    data.append(651612395876)

#This function inserts an element at the end of lists of different sizes
def listInsertLast(data): #appears to be linear - O(n)
    data.insert(-1, 651612395876)

#This function inserts an element at the beginning of lists of different sizes
def listInsertFirst(data): #appears to be linear - O(n)
    data.insert(0, 651612395876)

#This function inserts an element in the middle of lists of different sizes
def listInsertMiddle(data): #appears to be linear - O(n)
    middle = int(len(data) / 2)
    data.insert(middle, 651612395876)

#This function removes the last element from lists of different sizes
def listRemoveLast(data): #appears to be linear - O(n)
    data.remove(data[-1])

#This function removes the first element from lists of different sizes
def listRemoveFirst(data): #appears to be linear - O(n)
    data.remove(data[1])

#This function removes the middle element from lists of different sizes
def listRemoveMiddle(data): #appears to be linear - O(n)
    middle = int(len(data) / 2)
    data.remove(data[middle])

#This function searches for the last element in lists of different sizes
def listSearch(data): #appears to be linear - O(n)
    if data[-1] in data:
        return True
    else:
        return False

#This function adds a key and value to dictionaries of different sizes
def dictAppend(data): #adding a key and value to a dictionary appears to be constant
    data[651612395876] = 1

#This function tries to remove a key from dictionaries of different sizes
def dictRemove(data): #removing a key from a dictionary appears to be constant
    data.pop(651612395876, None)

#This function searches for a key in dictionaries of different sizes - should be run after dictAppend
def dictSearch(data): #in operator for searching dictionaries appear to be constant
    if 651612395876 in data:
        return True
    else:
        return False

def main():
    print("Running.")

main()
