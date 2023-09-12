def reverse_integer(n):
    # your implementation goes here

def reverse(data):
    # convert string into a list of characters
    data = list(data)
    # pointing to the first item
    start_index = 0
    # index pointing to the last item
    end_index = len(data) - 1
    while end_index > start_index:
        data[start_index], data[end_index] = data[end_index], data[start_index]
        start_index += 1
        end_index -= 1
    # transform the list of letters into a string
    return ''.join(data)

if __name__ == '__main__':
    print(is_palindrome('madam'))