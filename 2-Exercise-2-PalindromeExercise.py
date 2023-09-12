# you can define helper methods if needed
def is_palindrome(s):
    original_string = s
    reversed_string = reverse(s)

    if original_string == reversed_string:
        return True

    return False


def is_palindrome(s):
    start_index = 0
    end_index = len(s) - 1
    while end_index > start_index:
        if s[start_index] != s[end_index]:
            return False
        else:
            start_index += 1
            end_index -= 1

    return True


def reverse(data):
    # convert string into a list of characters
    data = list(data)
    # pointing to the first item
    start_index = 0
    # index pointing to the last item
    end_index = len(data)-1
    while end_index > start_index:
        data[start_index], data[end_index] = data[end_index], data[start_index]
        start_index += 1
        end_index -= 1
    # transform the list of letters into a string
    return ''.join(data)

if __name__ == '__main__':
    print(is_palindrome('madam'))









# def is_palindrome(s):
#     start_index = 0
#     end_index = len(s) - 1
#     while end_index > start_index:
#         if s[start_index] != s[end_index]:
#             return False
#         else:
#             start_index += 1
#             end_index -= 1
#
#     return True
