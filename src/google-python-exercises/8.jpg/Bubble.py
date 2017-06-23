def Bubble(alist):
    for a in range(len(alist)-1,0,-1):
        for i in range(a):
            if alist[i] > alist[i+1]:
                temp= alist[i]
                alist[i] = alist[i+1]
                alist[i+1] = temp
alist = [23,4,56,34,5,3,2]
Bubble(alist)
print alist


    