def find_longest_string(string_list):
    longest_string = ""
    for string in string_list:
        if len(string) > len(longest_string):
            longest_string = string
    return longest_string





string_list = ['apple', 'banana', 'kiwi', 'pear']
longest = find_longest_string(string_list)
print(longest)

"""
    EXPECTED OUTPUT:
    ----------------
    banana

"""