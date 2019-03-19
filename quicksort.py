#challenge python_quicksort
#reference https://ja.wikipedia.org/wiki/%E3%82%AF%E3%82%A4%E3%83%83%E3%82%AF%E3%82%BD%E3%83%BC%E3%83%88

import math
import random
import time

def get_median(x,y,z):
    if x < y:
        if y < z:
            return y
        elif z < x:
            return x
        else:
            return z
    else:
        if z < y:
            return y
        elif x < z:
            return x
        else:
            return z

def quicksort(sL,l,r):
    if(l < r):
        i = l
        j = r
        pivot = get_median(sL[i], sL[math.floor((i + (j - i) / 2))], sL[j])
        while True:
            while (sL[i] < pivot):
                i+=1
            while (pivot < sL[j]):
                j-=1
            if (i >= j):
                break
            tmp = sL[i]
            sL[i] = sL[j]
            sL[j] = tmp
            i+=1
            j-=1 
        quicksort(sL,l,i - 1)
        quicksort(sL,j + 1,r)

def create_testdata(s_list,_s_len):
    #Create an empty list for sorting
    s_list = []
    s_len = _s_len
    #Test data range
    rMin = 0
    rMax = 1000
    #Create data for sorting
    for i in range(s_len):
        s_list.append(random.randint(rMin,rMax))

    return s_list

def _quicksort(sL):
    
    #print('Before sorting : ' + ','.join(map(str,sL)))

    start = time.time()

    #Create Pivot
    left = 0
    right = len(sL) - 1

    quicksort(sL,left,right)
    #print('After sorting : ' + ','.join(map(str,sL)))

    elapsed_time = time.time() - start
    print ('Data ' + str(len(sL)) + ' :' + str(elapsed_time) + '[sec]')

if __name__ == '__main__':

    #Data preparation
    sortlist = []
    sortlist = create_testdata(sortlist,1000)
    _quicksort(sortlist)
    sortlist = create_testdata(sortlist,10000)
    _quicksort(sortlist)
    sortlist = create_testdata(sortlist,10000)
    _quicksort(sortlist)
    sortlist = create_testdata(sortlist,100000)
    _quicksort(sortlist)

    