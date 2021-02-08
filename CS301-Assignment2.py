#Assignment 2 - CS301
#Outline Created by Cody Cox
#Finished by Jacob Hardman
#2/7/2021
#Dr. Nathaniel Miller

import time

def bench(f, inp):
    t1 = time.time()
    f(inp)
    t2 = time.time()
    t = t2-t1
    return t

listData1k = list(open('data1k.txt').read().split())
listData10k = list(open('data10k.txt').read().split())
listData50k = list(open('data50k.txt').read().split())
listData100k = list(open('data100k.txt').read().split())
listData250k = list(open('data.250k.txt').read().split())
listData500k = list(open('data500k.txt').read().split())
listData750k = list(open('data750k.txt').read().split())
listData1m = list(open('data1m.txt').read().split())

dictData1k = {}
dictData10k = {}
dictData50k = {}
dictData100k = {}
dictData250k = {}
dictData500k = {}
dictData750k = {}
dictData1m = {}
for line in listData1k:
    if line not in dictData1k:
        dictData1k[line] = 1
for line in listData10k:
    if line not in dictData10k:
        dictData10k[line] = 1
for line in listData50k:
    if line not in dictData50k:
        dictData50k[line] = 1
for line in listData100k:
    if line not in dictData100k:
        dictData100k[line] = 1
for line in listData250k:
    if line not in dictData250k:
        dictData250k[line] = 1
for line in listData500k:
    if line not in dictData500k:
        dictData100k[line] = 1
for line in listData750k:
    if line not in dictData750k:
        dictData750k[line] = 1
for line in listData1m:
    if line not in dictData1m:
        dictData1m[line] = 1

listOfLists = [listData1k, listData10k, listData50k, listData100k, listData250k, listData500k, listData750k, listData1m]
listOfDicts = [dictData1k, dictData10k, dictData50k, dictData100k, dictData250k, dictData500k, dictData750k, dictData1m]
dataSize= [1000, 10000, 50000, 100000, 250000, 500000, 750000, 1000000]

def main():
    f_out = open("AppendingToListsData.csv", "w+")
    print("Testing Appending To Lists:")
    i = 0
    for lists in listOfLists:
        time = bench(listAppend, lists)
        f_out.write(str(dataSize[i]) + ",")
        f_out.write(str(time) + "\r\n")
        i += 1
    f_out.close()

    f_out = open("InsertingToTheEndOfListsData.csv", "w+")
    print("Testing Inserting To The End Of Lists:")
    i = 0
    for lists in listOfLists:
        time = bench(listInsertLast, lists)
        f_out.write(str(dataSize[i]) + ",")
        f_out.write(str(time) + "\r\n")
        i += 1
    f_out.close()

    f_out = open("InsertingToTheBeginningOfListsData.csv", "w+")
    print("Testing Inserting To Beginning Of Lists:")
    i = 0
    for lists in listOfLists:
        time = bench(listInsertFirst, lists)
        f_out.write(str(dataSize[i]) + ",")
        f_out.write(str(time) + "\r\n")
        i += 1
    f_out.close()

    f_out = open("InsertingToTheMiddleOfListsData.csv", "w+")
    print("Testing Inserting In The Middle Of Lists:")
    i = 0
    for lists in listOfLists:
        time = bench(listInsertMiddle, lists)
        f_out.write(str(dataSize[i]) + ",")
        f_out.write(str(time) + "\r\n")
        i += 1
    f_out.close()

    f_out = open("RemovingLastValueOfListsData.csv", "w+")
    print("Testing Removing Last Value Of Lists:")
    i = 0
    for lists in listOfLists:
        time = bench(listRemoveLast, lists)
        f_out.write(str(dataSize[i]) + ",")
        f_out.write(str(time) + "\r\n")
        i += 1
    f_out.close()

    f_out = open("RemovingFirstValueOfListsData.csv", "w+")
    print("Testing Removing First Value Of Lists:")
    i = 0
    for lists in listOfLists:
        time = bench(listRemoveFirst, lists)
        f_out.write(str(dataSize[i]) + ",")
        f_out.write(str(time) + "\r\n")
        i += 1
    f_out.close()

    f_out = open("RemovingMiddleValueOfListsData.csv", "w+")
    print("Testing Removing Middle Value Of Lists:")
    i = 0
    for lists in listOfLists:
        time = bench(listRemoveMiddle, lists)
        f_out.write(str(dataSize[i]) + ",")
        f_out.write(str(time) + "\r\n")
        i += 1
    f_out.close()

    f_out = open("SearchingListsData.csv", "w+")
    print("Testing Seaching Lists:")
    i = 0
    for lists in listOfLists:
        time = bench(listSearch, lists)
        f_out.write(str(dataSize[i]) + ",")
        f_out.write(str(time) + "\r\n")
        i += 1
    f_out.close()

    f_out = open("AppendingValueToDictsData.csv", "w+")
    print("Testing Appending Value To Dictionaries:")
    i = 0
    for dicts in listOfDicts:
        time = bench(dictAppend, dicts)
        f_out.write(str(dataSize[i]) + ",")
        f_out.write(str(time) + "\r\n")
        i += 1
    f_out.close()

    f_out = open("RemovingValuesFromDictsData.csv", "w+")
    print("Testing Removing Values From Dictionaries:")
    i = 0
    for dicts in listOfDicts:
        time = bench(dictRemove, dicts)
        f_out.write(str(dataSize[i]) + ",")
        f_out.write(str(time) + "\r\n")
        i += 1
    f_out.close()

    f_out = open("SearchingDictsData.csv", "w+")
    print("Testing Searching Dictionaries For Values:")
    i = 0
    for dicts in listOfDicts:
        time = bench(dictSearch, dicts)
        f_out.write(str(dataSize[i]) + ",")
        f_out.write(str(time) + "\r\n")
        i += 1
    f_out.close()

    print("\nAll benchmarks complete. Results have been written to CSV files.")

def listAppend(data):
    data.append(582394)

def listInsertLast(data):
    data.insert(-1, 489278)

def listInsertFirst(data):
    data.insert(0, 395835)

def listInsertMiddle(data):
    middle = int(len(data) / 2)
    data.insert(middle, 583927)

def listRemoveLast(data):
    data.remove(data[-1])

def listRemoveFirst(data):
    data.remove(data[1])

def listRemoveMiddle(data):
    middle = int(len(data) / 2)
    data.remove(data[middle])

def listSearch(data):
    if data[-1] in data:
        return True
    else:
        return False

def dictAppend(data):
    data[582956] = 1

def dictRemove(data):
    data.pop(651606, None)

def dictSearch(data):
    if 651616 in data:
        return True
    else:
        return False

main()
