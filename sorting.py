def swap(x,y):
    x,y=y,x

def bubbleSort(array):
    """Bubble Sort in pseudocode:

        begin BubbleSort(list)
       for all elements of list
          if list[i] > list[i+1]
             swap(list[i], list[i+1])
          end if
       end for
       return list
    end BubbleSort"""

    length = len(array)
    alreadyOrdered = True
    for i in range(length-1):
        for j in range(0,length-i-1):
            if array[j] > array[j+1]:
                array[j],array[j+1]=array[j+1],array[j]
                alreadyOrdered = False
        if alreadyOrdered:
            return array

    return array


def bubbleSort(array):
    """Bubble Sort in pseudocode:

        begin BubbleSort(list)
       for all elements of list
          if list[i] > list[i+1]
             swap(list[i], list[i+1])
          end if
       end for
       return list
    end BubbleSort"""

    length = len(array)
    alreadyOrdered = True
    for i in range(length-1):
        for j in range(0,length-i-1):
            if array[j] > array[j+1]:
                array[j],array[j+1] = array[j+1],array[j]
                alreadyOrdered = False
        if alreadyOrdered:
            return array
    return array