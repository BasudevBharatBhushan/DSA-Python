from linkedlist import ListNode

# Brute Force Approach | TC - O(N) + O(N/2) | SC - O(1)
def middle_of_linkedlist(head:ListNode)->ListNode:
    len = ListNode.length_linkedlist(head)

    mid = len // 2
    temp = head

    for i in range (mid):
        temp = temp.next

    return temp


# Tortoise and Hare Algorithm
def middle_of_linkedlist_optimal(head:ListNode)->ListNode:
    show = head
    fast = head
    while fast and fast.next and slow:
        fast = fast.next.next
        slow = slow.next

    return slow





# Test Cases
head = ListNode(1)
head.next = ListNode(2)
head.next.next = ListNode(3)
head.next.next.next = ListNode(4)
head.next.next.next.next = ListNode(5)
# head.next.next.next.next.next = ListNode(6)
ListNode.print_linkedlist(middle_of_linkedlist(head)) 
