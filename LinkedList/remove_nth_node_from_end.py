from linkedlist import ListNode

def remove_nth_node_from_end(head:ListNode, n:int)->ListNode:

    len = ListNode.length_linkedlist(head)

    if len == 1:
        return None
    
    ind_to_be_removed = len - n

    temp = head

    while temp is not None:
        if ind_to_be_removed == 1:
            temp.next = temp.next.next
            break
        temp = temp.next
        ind_to_be_removed -= 1

    return head


def remove_nth_node_optimal(head:ListNode, n:int)->ListNode:
    fastp = head
    slowp = head

    for i in range(n):
        fastp = fastp.next

    if fastp is None:
        return head.next
    
    while fastp.next is not None:
        fastp = fastp.next
        slowp = slowp.next

    delNode = slowp.next
    slowp.next = slowp.next.next

    delNode = None

    return head



# Test Cases
head = ListNode(1)
head.next = ListNode(2)
head.next.next = ListNode(3)
head.next.next.next = ListNode(4)
head.next.next.next.next = ListNode(5)

ListNode.print_linkedlist(remove_nth_node_from_end(head, 2))
