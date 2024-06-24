from linkedlist import ListNode

"""
Given two linkedlist are sorrted in non-decreasing order, merge them in sorted order

"""
# Brute Force, Convert to Arr and sort | TC - O(N1+N2) + O(NLogN) + O(N) | SC - O(N)
def merge_two_list(list1:ListNode, list2:ListNode)->ListNode:
    arr = []

    temp1 = list1
    temp2 = list2

    while temp1 is not None:
        arr.append(temp1.val)
        temp1 = temp1.next

    while temp2 is not None:
        arr.append(temp2.val)
        temp2 = temp2.next

    arr.sort()

    dummy_node = ListNode(-1)

    temp = dummy_node
    for i in range (len(arr)):
        temp.next = ListNode(arr[i])
        temp = temp.next

    return dummy_node.next


# Optimal Approach | TC - O(N1+N2) | SC - O(1)

def merge_two_list_optimal(list1:ListNode, list2:ListNode)->ListNode:

    dummy_node = ListNode(-1)

    temp = dummy_node

    while list1 is not None and list2 is not None:
        if list.data <= list2.data:
            temp.next = list1list1 = list1.next
        else:
            temp.next = list2list2 = list2.next

        temp = temp.next



    if list1 is not None:
        temp.next = list1
    else:
        temp.next = list2


    return dummy_node.next
