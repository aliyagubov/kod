# Python program to count all substrings that start 
# and end with '1' using Brute-Force Approach

# Function to count valid substrings
def binarySubstring(s):
    
    n = len(s)
    count = 0

    # Traverse all substrings using nested loops
    for i in range(n):

        # If starting character is '1'
        if s[i] == '1':

            for j in range(i + 1, n):

                # If ending character is also '1'
                if s[j] == '1':

                    count += 1

    return count

# Driver code
if __name__ == "__main__":

    s = "00100101"

    print(binarySubstring(s))