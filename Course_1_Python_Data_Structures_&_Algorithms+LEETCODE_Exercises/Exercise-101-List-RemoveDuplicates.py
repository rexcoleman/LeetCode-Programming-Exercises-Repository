def remove_duplicates(nums):
    if not nums:
        return 0
    write_pointer = 1
    for read_pointer in range(1, len(nums)):
        if nums[read_pointer] != nums[read_pointer - 1]:
            nums[write_pointer] = nums[read_pointer]
            write_pointer += 1
    return write_pointer


nums = [0, 0, 1, 1, 1, 2, 2, 3, 3, 4]
new_length = remove_duplicates(nums)
print("New length:", new_length)
print("Unique values in list:", nums[:new_length])
# print(nums)

"""
    EXPECTED OUTPUT:
    ----------------
    New length: 5
    Unique values in list: [0, 1, 2, 3, 4]

"""