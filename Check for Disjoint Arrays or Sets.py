# Python program to check if the given arrays are disjoint
# using two nested loops

def areDisjoint(a, b):
    
    # Take every element of array a 
    # and search it in array b
    for i in range(len(a)):
        for j in range(len(b)):
            
            # If any common element is found
            # given arrays are not disjoint
            if a[i] == b[j]:
                return False
    
    return True

a = [12, 34, 11, 9, 3]
b = [7, 2, 1, 5]

if areDisjoint(a, b):
    print("True")
else:
    print("False")