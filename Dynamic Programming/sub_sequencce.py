# Hello World program in Python

import numpy as np    
nums = [5,7,4,-3,9,1,10,4,5,8,9,3]
def subsequence(nums):
    #L = np.zeros(len(nums))
    L = []
    for i in range(0,len(nums)):
        L.append(1)
        #L[i] = 1
        for j in range(0,i):
            if nums[j]<nums[i] and L[i]<1+L[j]:
                L[i] = 1+ L[j]
    
    maxval = 1
    for i in range(1,len(nums)):
        if L[i]>L[maxval]:
            maxval = i
    
    print(L)
    return L[maxval]
    
print(subsequence(nums))