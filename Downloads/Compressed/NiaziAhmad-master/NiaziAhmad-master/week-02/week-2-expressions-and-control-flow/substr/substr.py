#  Create a function that takes two strings as a parameter
#  Returns the starting index where the second one is starting in the first one
#  Returns `-1` if the second string is not in the first one

def substr(str, substr):
    substr_len = len(substr)
    str_len = len(str)

    for i in range(str_len - substr_len + 1):
        for j in range(substr_len):
            if str[i + j] != substr[j]:
                break
        if j + 1 == substr_len:
            return i
    return -1


#  Example
# should print: `17`
print(substr("this is what I'm searching in", "searching"))

# should print: `-1`
print(substr("this is what I'm searching in", "not"))
