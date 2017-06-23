def search(alist,item):
    position = 0
    found = False

    while position<len(alist) and not found:
        if alist[position]==item:
            found = True
        else:
            position = position+1
    return found


a = [2,3,4,5,6,7,8,9,9,98,76]

print (search(a,5))

