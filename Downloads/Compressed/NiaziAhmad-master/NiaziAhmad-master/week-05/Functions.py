base_number = 123


def double_number(number):
    return number * number


print("###############################")
print("Output of Fuction double_number(number)")
print(f"base number:{base_number} returned numbe: {double_number(base_number)}")

##############
al = "Green Fox"


def greet(greet):
    print(f"Greetings dear {greet}")


print("###############################")
print("Output of Fuction greet(greet)")
greet(al)

#############

typo = "Chinchill"


def append_a(str):
    return str + "a"


print("###############################")
print("Output of Fuction append_a(str)")
print(append_a(typo))


####################

def sum(num):
    total = 0
    for i in range(num + 1):
        total += i
    return total


print("###############################")
print("Output of Fuction sum(num)")
print(sum(100))


#######################
def calculateFactorial(num):
    f = 1
    for i in range(1, num + 1):
        f *= i
    return f


print("###############################")
print("Output of Fuction calculateFactorial(num)")
print(calculateFactorial(15))


########################
def find_matching_indexes(num, num_list):
    string = str(num_list)
    num = str(num)
    index = []
    for i in range(len(num_list)):
        temp = str(num_list[i])
        a = temp.rfind(num) > -1
        if a:
            index.append(i)
    return index


print("###############################")
print("Output of Fuction find_matching_indexes(num, num_list)")
print(find_matching_indexes(1, [1, 11, 34, 52, 61]))

print(find_matching_indexes(9, [1, 11, 34, 52, 61]))


###########################
def find_unique_items(arr):
    temp = {arr[0]}
    for i in arr:
        temp.add(i)
    return sorted(list(temp))


print("###############################")
print("Output of Fuction find_unique_items(arr)")
print(find_unique_items([1, 11, 34, 11, 52, 61, 1, 34]))


def isAnagram(str1, str2):
    if len(str1) == len(str2):
        str1 = str1.lower()
        str2 = str2.lower()
        if sorted(str1) == sorted(str2):
            return True
    return False


print("###############################")
print("Output of Fuction isAnagram(str1, str2)")
print(isAnagram("Dog", "ogd"))


def searchPalindrome(str):
    temp = []
    for i in range(len(str)):
        for j in range(i + 3, len(str)):
            if str[i:j] == str[i:j][::-1]:
                temp.append(str[i:j])
    return temp


print("###############################")
print("Output of Fuction searchPalindrome(str)")
print(searchPalindrome("dog goat dad duck doodle never"))


def bubble(nums):
    for i in range(len(nums)):
        for j in range(len(nums) - i - 1):
            if nums[j] > nums[j + 1]:
                nums[j], nums[j + 1] = nums[j + 1], nums[j]
    return nums


def advanced_bubble(nums, is_descending):
    if is_descending:
        for i in range(len(nums)):
            for j in range(len(nums) - i - 1):
                if nums[j] < nums[j + 1]:
                    nums[j], nums[j + 1] = nums[j + 1], nums[j]
        return nums
    else:
        return bubble(nums)


print("###############################")
print("Output of Fuction bubble(nums)")
print(bubble([43, 12, 24, 9, 5]))
print(advanced_bubble([43, 12, 24, 9, 5], True))
