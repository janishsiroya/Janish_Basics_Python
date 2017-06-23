def Binary(alist,item):
    first = 0
    found = False
    last = len(alist)-1
    while first<=last and not found:
        middle = (first +last)/2
        if alist[middle] == item:
            found = True
        else:
            if item <alist[middle]:
                last = middle-1
            else:
                first = middle+1
    return found

a = [1,2,3,4,5,6,7,8,9]
print Binary(a,6)
print Binary(a,10)