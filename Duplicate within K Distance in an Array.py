def check_duplicates_within_k(arr, k):
    n = len(arr)

    # Traverse for every element
    for i in range(n):
      
        # Traverse next k elements
        for c in range(1, k + 1):
            j = i + c
            
            # If we find one more occurrence within k
            if j < n and arr[i] == arr[j]:
                return True
              
    return False

# Driver method to test above method
arr = [10, 5, 3, 4, 3, 5, 6]
print("Yes" if check_duplicates_within_k(arr, 3) else "No")