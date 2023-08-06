def has_unique_chars(string):
    char_set = set()
    for char in string:
        if char in char_set:
            return False
        char_set.add(char)
    return True


# def has_unique_chars(list1):
#     list2 = list(set(list1))
#     if len(list1) == len(list2):
#         return True
#     else:
#         return False


print(has_unique_chars('abcdefg'))  # should return True
print(has_unique_chars('hello'))  # should return False
print(has_unique_chars(''))  # should return True
print(has_unique_chars('0123456789'))  # should return True
print(has_unique_chars('abacadaeaf'))  # should return False

"""
    EXPECTED OUTPUT:
    ----------------
    True
    False
    True
    True
    False

"""