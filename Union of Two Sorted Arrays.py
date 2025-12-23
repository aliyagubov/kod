# Python program to find union of two arrays
# using nested loops

def findUnion(a, b):
    res = []
    
    # Traverse through a[] and search every element
    # a[i] in result
    for i in range(len(a)):
      
        # check if the element is already 
        # in the result to avoid duplicates
        if a[i] not in res:
            res.append(a[i])
    
    # Traverse through b[] and search every element
    # b[i] in result
    for i in range(len(b)):
      
        # check if the element is already 
        # in the result to avoid duplicates
        if b[i] not in res:
            res.append(b[i])
    
    res.sort()
    return res

if __name__ == "__main__":
    a = [1, 1, 2, 2, 2, 4]
    b = [2, 2, 4, 4]

    res = findUnion(a, b)
    
    for i in res:
        print(i, end=" ")