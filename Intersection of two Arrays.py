def intersect(a, b):
    res = []

    # Traverse through a[] and 
    # search every element a[i] in b[]
    for i in a:
        for j in b:
          
            # If found, check if the element
            # is already in the result
            if i == j and i not in res:
                res.append(i)
                
    return res

if __name__ == "__main__":
    a = [1, 2, 3, 2, 1]
    b = [3, 2, 2, 3, 3, 2]

    res = intersect(a, b)

    print(" ".join(map(str, res)))