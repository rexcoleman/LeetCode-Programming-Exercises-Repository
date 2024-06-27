def find_duplicates(nums):
    num_counts = {}
    for num in nums:
        num_counts[num] = num_counts.get(num, 0) + 1
    duplicates = [num for num, count in num_counts.items() if count > 1]
    return duplicates


# def find_duplicates(list1):
#     list2 = []
#     list3 = []
#     for i in list1:
#         if i in list2:
#             if i not in list3:
#                 list3.append(i)
#         list2.append(i)
#     return list3


print ( find_duplicates([1, 2, 3, 4, 5]) )
print ( find_duplicates([1, 1, 2, 2, 3]) )
print ( find_duplicates([1, 1, 1, 1, 1]) )
print ( find_duplicates([1, 2, 3, 3, 3, 4, 4, 5]) )
print ( find_duplicates([1, 1, 2, 2, 2, 3, 3, 3, 3]) )
print ( find_duplicates([1, 1, 1, 2, 2, 2, 3, 3, 3, 3]) )
print ( find_duplicates([]) )



"""
    EXPECTED OUTPUT:
    ----------------
    []
    [1, 2]
    [1]
    [3, 4]
    [1, 2, 3]
    [1, 2, 3]
    []

"""

