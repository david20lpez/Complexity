# -*- coding: utf-8 -*-
import time
import random
import copy

comparacionesQ = 0
cambiosQ = 0

comparacionesM = 0
cambiosM = 0

comparacionesB = 0
cambiosB = 0

def randomVec():
    i = 0
    v = [0]*100
    while(i < len(v)):
        v[i] = random.randint(0, 9999)
        i = i + 1
    return v

def bubbleSort(arr, n):
    i = 0
    k = 0
    j = 0
    global comparacionesB 
    global  cambiosB 
    while(i < n-1):
        while(j < n-i-1):
            if(arr[j] > arr[j+1]):
                k = arr[j]
                arr[j] = arr[j+1]
                arr[j+1] = k
                cambiosB = cambiosB + 1
            comparacionesB = comparacionesB + 1
            j = j + 1
        j = 0
        i = i + 1


def partition(arr,low,high): 
    i = ( low-1 )         # index of smaller element 
    pivot = arr[high]     # pivot 
    global comparacionesQ
    global cambiosQ
    for j in range(low , high): 
  
        # If current element is smaller than the pivot 
        if   arr[j] < pivot: 
          
            # increment index of smaller element 
            i = i+1 
            arr[i],arr[j] = arr[j],arr[i] 
            cambiosQ = cambiosQ + 1
        comparacionesQ = comparacionesQ + 1
    arr[i+1],arr[high] = arr[high],arr[i+1] 
    cambiosQ = cambiosQ + 1
    return ( i+1 )
  
# The main function that implements QuickSort 
# arr[] --> Array to be sorted, 
# low  --> Starting index, 
# high  --> Ending index 
  
# Function to do Quick sort 

def quickSort(arr,low,high):
    if low < high: 
        # pi is partitioning index, arr[p] is now 
        # at right place 
        pi = partition(arr,low,high)
        # Separately sort elements before 
        # partition and after partition 
        quickSort(arr, low, pi-1) 
        quickSort(arr, pi+1, high)

# Python program for implementation of MergeSort 
def mergeSort(arr):
    global comparacionesM
    global cambiosM 

    if len(arr) >1: 
        mid = len(arr)//2 #Finding the mid of the array 
        L = arr[:mid] # Dividing the array elements  
        R = arr[mid:] # into 2 halves 
  
        mergeSort(L) # Sorting the first half 
        mergeSort(R) # Sorting the second half 
  
        i = j = k = 0
          
        # Copy data to temp arrays L[] and R[] 
        while i < len(L) and j < len(R): 
            comparacionesM = comparacionesM + 1
            if L[i] < R[j]: 
                arr[k] = L[i] 
                cambiosM = cambiosM + 1
                i+=1
            else: 
                arr[k] = R[j] 
                cambiosM = cambiosM + 1
                j+=1
            k+=1
          
        # Checking if any element was left 
        while i < len(L): 
            arr[k] = L[i] 
            cambiosM = cambiosM + 1
            i+=1
            k+=1
          
        while j < len(R): 
            arr[k] = R[j] 
            cambiosM = cambiosM + 1
            j+=1
            k+=1

def linearSearch(arr, x):
    posicion = 0
    i = 0
    while(i<len(arr)):
        if(arr[i]==x):
            posicion = i
            break
        i = i + 1
    print("LinearSearch:")
    print("Elementos recorridos: " + str(i))
    if(posicion == 0):
        return -1
    else:
        return posicion

# Python code to implement iterative Binary  
# Search. 
  
# It returns location of x in given array arr  
# if present, else returns -1 
def binarySearch(arr, l, r, x): 
    recorridos = 0
    while l <= r: 
        recorridos = recorridos + 1
        mid = int(l + (r - l)/2)
          
        # Check if x is present at mid 
        if arr[mid] == x: 
            print("BinarySearch:")
            print("Elementos recorridos: " + str(recorridos))
            return mid 
  
        # If x is greater, ignore left half 
        elif arr[mid] < x: 
            l = mid + 1
  
        # If x is smaller, ignore right half 
        else: 
            r = mid - 1

    print("BinarySearch:")
    print("Elementos recorridos: " + str(recorridos))
    # If we reach here, then the element 
    # was not present 
    return -1

def averageQuick(arr):
    global comparacionesQ
    global cambiosQ
    total = 0
    i = 0
    j = 0
    copies = []
    while(j < 10):
        copies.append(copy.deepcopy(arr))
        j = j + 1

    while(i < 10):
        comparacionesQ = 0
        cambiosQ = 0
        startQuick = time.perf_counter() 
        quickSort(copies[i], 0, len(arr)-1)
        endQuick = time.perf_counter()
        total = total + endQuick - startQuick
        i = i + 1
    quickSort(arr, 0, len(arr)-1)
    return total/10

def averageBubble(arr):
    total = 0
    i = 0
    j = 0
    copies = []
    global comparacionesB
    global cambiosB
    while(j < 10):
        copies.append(copy.deepcopy(arr))
        j = j + 1

    while(i < 10):
        comparacionesB = 0
        cambiosB = 0
        startBubble = time.perf_counter() 
        bubbleSort(copies[i], len(arr))
        endBubble = time.perf_counter()
        total = total + endBubble - startBubble
        i = i + 1
    bubbleSort(arr, len(arr))
    return total/10
    
def averageMerge(arr):
    global comparacionesM
    global cambiosM
    total = 0
    i = 0
    j = 0
    copies = []
    while(j < 10):
        copies.append(copy.deepcopy(arr))
        j = j + 1

    while(i < 10):
        comparacionesM = 0
        cambiosM = 0
        startMerge = time.perf_counter() 
        mergeSort(copies[i])
        endMerge = time.perf_counter()
        total = total + endMerge - startMerge
        i = i + 1
    mergeSort(arr)
    return total/10


vec = randomVec()
arr = copy.deepcopy(vec)
arr2 = copy.deepcopy(vec)

print("Bubble takes: " + str(averageBubble(vec)))
print("Comparaciones Bubble: " + str(comparacionesB))
print("Cambios Bubble: "+ str(cambiosB))

# startBubble = time.perf_counter() 
# bubbleSort(vec, len(vec))
# endBubble = time.perf_counter()
# print("Comparaciones Bubble: " + str(comparacionesB))
# print("Cambios Bubble: "+ str(cambiosB))
# print(str(endBubble - startBubble) + ": seconds")

# startQuick = time.perf_counter() 
# quickSort(vec,0,len(vec)-1)
# endQuick = time.perf_counter()
# print("Comparaciones Quick: " + str(comparacionesQ))
# print("Cambios Bubble: "+ str(cambiosQ))
# print(str(endQuick - startQuick) + ": seconds")

print("Quick takes: " + str(averageQuick(arr)))
print("Comparaciones Quick: " + str(comparacionesQ))
print("Cambios Quick: "+ str(cambiosQ))

print("Merge takes: " + str(averageMerge(arr2)))
print("Comparaciones Merge: " + str(comparacionesM))
print("Cambios Merge: "+ str(cambiosM))

x = input("Inserte un número: ")
startLinear = time.perf_counter()
print("El elemento está en la posición: "+ str(linearSearch(arr2,int(x))))
endLinear = time.perf_counter()
print("Time =", endLinear - startLinear, "seconds")

startBinary = time.perf_counter()
print("El elemento está en la posición: "+ str(binarySearch(arr2,0,len(vec)-1,int(x))))
endBinary = time.perf_counter()
print("Time =", endBinary - startBinary, "seconds")


