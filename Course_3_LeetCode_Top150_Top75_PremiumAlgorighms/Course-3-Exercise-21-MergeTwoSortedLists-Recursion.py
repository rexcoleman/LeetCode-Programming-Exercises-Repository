class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution(object):
    def mergeTwoLists(self, list1, list2):
        """
        :type list1: Optional[ListNode]
        :type list2: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        if list1 is None:
            return list2
        if list2 is None:
            return list1
        elif list1.val <= list2.val:
            list1.next = self.mergeTwoLists(list1.next, list2)
            return list1
        else:
            list2.next = self.mergeTwoLists(list1, list2.next)
            return list2

def list_to_linkedlist(lst):
    dummy = ListNode(0)
    current = dummy
    for val in lst:
        current.next = ListNode(val)
        current = current.next
    return dummy.next

def linkedlist_to_list(head):
    result = []
    current = head
    while current:
        result.append(current.val)
        current = current.next
    return result

if __name__ == '__main__':
    solution = Solution()

    list1_1 = [1, 2, 4]
    list1_2 = [1, 3, 4]
    list2_1 = []
    list2_2 = []
    list3_1 = []
    list3_2 = [0]

    linked_list1_1 = list_to_linkedlist(list1_1)
    linked_list1_2 = list_to_linkedlist(list1_2)
    linked_list2_1 = list_to_linkedlist(list2_1)
    linked_list2_2 = list_to_linkedlist(list2_2)
    linked_list3_1 = list_to_linkedlist(list3_1)
    linked_list3_2 = list_to_linkedlist(list3_2)

    outcome1_head = solution.mergeTwoLists(linked_list1_1, linked_list1_2)
    outcome1_list = linkedlist_to_list(outcome1_head)
    outcome2_head = solution.mergeTwoLists(linked_list2_1, linked_list2_2)
    outcome2_list = linkedlist_to_list(outcome2_head)
    outcome3_head = solution.mergeTwoLists(linked_list3_1, linked_list3_2)
    outcome3_list = linkedlist_to_list(outcome3_head)

    print(f"Outcome1: {outcome1_list}")
    print(f"Outcome2: {outcome2_list}")
    print(f"Outcome3: {outcome3_list}")


















# # Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
#
# class LinkedList():
#     def __init__(self, x):
#         new_node = ListNode(x)
#         self.head = new_node
#         self.tail = new_node
#         self.length = 1
#
#     def append(self, x):
#         new_node = ListNode(x)
#         if self.length == 0:
#             self.head = new_node
#             self.tail = new_node
#         else:
#             self.tail.next = new_node
#             self.tail = new_node
#         self.length += 1
#
#     def pop_first(self):
#         if self.length == 0:
#             return None
#         temp = self.head
#         self.head = self.head.next
#         temp.next = None
#         self.length -= 1
#         if self.length == 0:
#             self.tail = None
#         return temp
#
#     def print_list(self):
#         temp = self.head
#         while temp is not None:
#             print(temp.val)
#             temp = temp.next
#
#     def convert_list_to_linked_list(self, list):
#         if len(list) <= 1:
#             return
#         for i in range(1,len(list)):
#             self.append(list[i])
#
#     def to_list(self):
#         result = []
#         temp = self.head
#         while temp is not None:
#             result.append(temp.val)
#             temp = temp.next
#         return result
#
#
# class Solution(object):
#     def mergeTwoLists(self, list1, list2):
#         """
#         :type list1: Optional[ListNode]
#         :type list2: Optional[ListNode]
#         :rtype: Optional[ListNode]
#         """
#         if list1 is None:
#             return list2
#         if list2 is None:
#             return list1
#         elif list1.val <= list2.val:
#             list1.next = self.mergeTwoLists(list1.next, list2)
#             return list1
#         else:
#             list2.next = self.mergeTwoLists(list1, list2.next)
#             return list2
#
#
# if __name__ == '__main__':
#
#     solution = Solution()
#
#     list1_1 = [1, 2, 4]
#     list1_2 = [1, 3, 4]
#     list2_1 = []
#     list2_2 = []
#     list3_1 = []
#     list3_2 = [0]
#
#     linked_list1_1 = LinkedList(list1_1[0])
#     linked_list1_1.convert_list_to_linked_list(list1_1)
#     linked_list1_1.print_list()
#     linked_list1_2 = LinkedList(list1_2[0])
#     linked_list1_2.convert_list_to_linked_list(list1_2)
#     linked_list1_2.print_list()
#     outcome1_head = solution.mergeTwoLists(linked_list1_1.head, linked_list1_2.head)
#
#
#     outcome1_list = LinkedList(outcome1_head).to_list()
#
#     print(outcome1_list)
#     print(outcome1_list[0])