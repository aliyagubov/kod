def isSubset(a, b):
    m, n = len(a), len(b)
    
    for i in range(n):
        found = False
        for j in range(m):
            if b[i] == a[j]:
                found = True
                a[j] = -1  # mark as visited
                break
        if not found:
            return False
    return True

if __name__ == '__main__':
    a = [11, 1, 13, 21, 3, 7]
    b = [11, 3, 7, 1]
    
    if isSubset(a, b):
        print("true")
    else:
        print("false")