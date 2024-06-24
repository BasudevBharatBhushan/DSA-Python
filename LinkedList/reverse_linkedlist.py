from linkedlist import ListNode

    

def reverse_linkedlist(head:ListNode)->ListNode:

    temp = head
    stack = []


    while temp is not None:
        stack.append(temp.val)
        temp = temp.next

    
    temp = head

    while temp is not None:
        temp.val = stack.pop()
        temp = temp.next

    return head



# Optimal Approach | TC - O(N) | SC - O(1)

def reverse_linkedlist_optimal(head:ListNode)->ListNode:
    temp = head
    prev = None

    while temp is not None:
        front = temp.next

        temp.next = prev

        prev = temp

        temp = front

    return prev


# Optimal Approach | Using Recursion | TC - O(N) | SC - O(1)
def reverse_linkedlist_recursive(head:ListNode)->ListNode:

    if head is None or head.next is None:
        return head
    
    new_head = reverse_linkedlist_recursive(head.next)

    front = head.next
    front.next = head
    head.next = None

    return new_head



# Test Cases


# Creating the linked list
head = ListNode(1)
head.next = ListNode(2)
head.next.next = ListNode(3)
head.next.next.next = ListNode(4)

ListNode.print_linkedlist(head) # 1 2 3 4