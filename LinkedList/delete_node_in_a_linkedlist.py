from linkedlist import ListNode

"""
We are not given access to the entire linkedlist, just the node that needs to be deleted.

"""

def deleteNode(node:ListNode)->ListNode:


    node.val = node.next.val
    node.next = node.next.next

