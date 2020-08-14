def sum(array):
    sum=0
    for i in range(len(array)):
        sum+=array[i]
    return sum

def max(array):
    maximum=0
    for i in range(len(array)):
        if array[i]>maximum:
            maximum=array[i]
    return maximum

def min(array):
    minimum=0
    for i in range(len(array)):
        if array[i]<minimum:
            minimum=array[i]
    return minimum

def contains(array,value):
    for i in range(len(array)):
        if array[i]==value:
            return True
    return False

def occurrency(array,value):
    occ=0
    for i in range(len(array)):
        if array[i]==value:
            occ+=1
    return occ

def inAscendingOrder(array):
    for i in range(len(array)-1):
        if array[i]>array[i+1]:
            return False
    return True

def inDescendingOrder(array):
    for i in range(len(array)-1):
        if array[i]<array[i+1]:
            return False
    return False

def greaterThan(array,value):
    for i in range(len(array)):
        if array[i]<=value:
            return False
    return True

def lowerThan(array,value):
    for i in range(len(array)):
        if array[i]>=value:
            return False
    return True

def allEqual(array):
    for e in array:
        if e!=array[0]:
            return False
    return True

