def remDuplicate(arr):
    res = []

    for i in range(len(arr)):

        # Check if this element is included in result
        j = 0
        while j < i:
            if arr[i] == arr[j]:
                break
            j += 1

        # Include this element if not included previously
        if i == j:
            res.append(arr[i])

    return res

if __name__ == "__main__":
    arr = [2, 2, 3, 3, 7, 5]
    res = remDuplicate(arr)
    for val in res:
        print(val, end=" ")