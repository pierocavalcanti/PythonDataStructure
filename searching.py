def linearSearch(list_,key_):
    """binary search
    return: None if not found, index of the first founded element otherwise"""
    for i in range(0,len(list_)):
        if list_[i] == key_:
            return i
    return None

def binarySearch(list_,key_):
    """binary search
    return: None if not found, index of the first founded element otherwise"""

    list_.sort()
    right = len(list_)-1
    left = 0
    notFound = True
    index = None

    while(left<=right and notFound):
        middle = (left+right)//2
        print(middle)
        if middle is key_:
            notFound = True
            index = middle
        else:
            if key_ <list_[middle]:
                right = middle - 1
            else:
                left = middle + 1

    return None if notFound else index