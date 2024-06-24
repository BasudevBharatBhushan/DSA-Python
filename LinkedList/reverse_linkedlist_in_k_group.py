"""
Input: head = [1,2,3,4,5], k = 2
Output: [2,1,4,3,5]
"""

"""

I will revisit this problem later to understand and practise again


"""

# TC - O(2N) | SC - O(1)
from linkedlist import ListNode 

def reverseKGroup(head:ListNode, k:int)->ListNode:

    temp = head
    prevLast = None


    while temp is not None:

        kth_node = move_by_k_nodes(temp, k)

        if kth_node is None:

            if prevLast:
                prevLast.next = temp

            break

            
        next_node = kth_node.next

        # Disconnect the node to reverse it
        kth_node.next = None


        reverse_linkedlist(temp)


        if temp is head:
            head = kth_node

        else:

            prevLast.next = kth_node

        
        prevLast = temp

        temp = next_node

    return head



def move_by_k_nodes(head:ListNode, k:int)->ListNode:

    k-=1

    while k > 0:
        head = head.next
        k-=1

        if head is None:
            return None

    return head


def reverse_linkedlist(head:ListNode)->ListNode:

    temp = head
    prev = 0

    while temp is not None:

        front = temp.next

        temp.next = prev

        prev = temp

        temp = front


    return prev


# Test Cases

head = ListNode(1)
head.next = ListNode(2)
head.next.next = ListNode(3)
head.next.next.next = ListNode(4)
head.next.next.next.next = ListNode(5)

head = reverseKGroup(head, 2)

ListNode.print_linkedlist(head)