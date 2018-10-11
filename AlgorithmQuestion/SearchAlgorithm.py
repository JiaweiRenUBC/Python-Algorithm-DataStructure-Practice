
# coding: utf-8

# In[1]:


def binarySearch(listGiven, target):
    start = 0
    finish =len(listGiven)-1
    # empty list given also represent not found
    if finish == -1:
        return -1
    else:
        midpoint = (start + finish) // 2
        if listGiven[midpoint] == target:
            return target
        if listGiven[midpoint] > target:
            return binarySearch(listGiven[:midpoint], target)
        if listGiven[midpoint] < target:
            return binarySearch(listGiven[midpoint + 1:], target)
        
testlist = [0, 1, 2, 8, 13, 17, 19, 32, 42,]
print(binarySearch(testlist, 3))
print(binarySearch(testlist, 13))

