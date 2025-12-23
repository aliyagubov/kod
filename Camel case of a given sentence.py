# Python program to convert given sentence to camel case

def convertToCamelCase(s):
    res = []

    # Flag to indicate when to capitalize the next letter
    capitalizeNext = False

    for i in range(len(s)):

        # If we encounter a space, set the flag to capitalize
        # the next character
        if s[i] == ' ':
            capitalizeNext = True

        # If the flag is set, capitalize the current character
        elif capitalizeNext:
            res.append(s[i].upper())

            # Reset the flag after capitalization
            capitalizeNext = False

        # Otherwise, just add the current character to the result
        else:
            res.append(s[i])

    return ''.join(res)

if __name__ == "__main__":
	s = "i got intern at geeksforgeeks"
	print(convertToCamelCase(s))