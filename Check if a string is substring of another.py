# Python program to check if a string is a substring of another
# using nested loops

# Function to find if pat is a substring of txt
def findSubstring(txt, pat):
    n = len(txt)
    m = len(pat)

    # Iterate through txt
    for i in range(n - m + 1):

        # Check for substring match
        j = 0
        while j < m and txt[i + j] == pat[j]:
            j += 1
        
        # If we completed the inner loop, we found a match
        if j == m:
            return i

    # No match found
    return -1

if __name__ == "__main__":
    txt = "geeksforgeeks"
    pat = "eks"
    print(findSubstring(txt, pat))