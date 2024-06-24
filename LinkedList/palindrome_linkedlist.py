from linkedlist import ListNode
from collections import deque

def is_palindrome(head:ListNode)->bool:
    st = deque()


    temp = head

    while temp is not None:

        st.append(temp.val)

        temp = temp.next


    temp = head


    while temp is not None:
        if temp.val != st.pop():
            return False
        temp = temp.next
        
    return True


# Tortoise and Hare Algorithm

def reverse_linkedlist(head:ListNode)->ListNode:
    
    if head is None or head.next is None:
        return head
    
    new_head = reverse_linkedlist(head.next)

    front = head.next

    front.next = head
    head.next = None

    return new_head

def is_palindrome(head:ListNode)->bool:

    if head is None or head.next is None:
        return True
    
    slow = head
    fast = head

    while fast.next is not None and fast.next.next is not None:
        slow = slow.next
        fast = fast.next.next


    new_head = reverse_linkedlist(slow.next)


    first = head

    second = new_head

    while second is not None:

        if first.data != second.data:
            return False
        
        first = first.next
        second = second.next




    return True