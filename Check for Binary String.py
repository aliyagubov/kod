# Python Program to check if a string is 
# binary string or not

def isBinary(s):
    for i in range(len(s)):
      
        # Check if the character is neither 
        # '0' nor '1'
        if s[i] != '0' and s[i] != '1':
            return False
    return True

s = "01010101010"
print("true" if isBinary(s) else "false")