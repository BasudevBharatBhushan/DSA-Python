"""
Input: intersectVal = 2, listA = [1,9,1,2,4], listB = [3,2,4], skipA = 3, skipB = 1
Output: Intersected at '2'

One Approach I could see is trversing the two linkedlist from the end and at one point there will be differnct node value, so the node after that will be the intersection point
"""

from linkedlist import ListNode
from typing import Optional


# Brute force approach | TC - O(N^2) | SC - O(1)
def getIntersectionNode(headA:ListNode, headB:ListNode)->Optional[ListNode]:

    while headB is not None:
        temp = headA
        while temp is not None:
            if temp == headB:
                return headB
            temp = temp.next
        headB = headB.next


    return None



# Hashing Approach | TC - O(N+M) | SC - O(N)

def getIntersectionNode_hashing(headA:ListNode, headB:ListNode)->Optional[ListNode]:
    st = set()

    while headA is not None:
        st.add(headA)
        headA = headA.next

    while headB is not None:
        if headB in st:
            return headB
        headB = headB.next

    return None


# Difference of length approach | TC - O(N+M) | SC - O(1)

def getIntersectionNode_diff(headA:ListNode, headB:ListNode)->Optional[ListNode]:
    lenA = ListNode.length_linkedlist(headA)
    lenB = ListNode.length_linkedlist(headB)

    if lenA > lenB:
        for i in range(lenA-lenB):
            headA = headA.next
    else:
        for i in range(lenB-lenA):
            headB = headB.next

    while headA is not None and headB is not None:
        if headA == headB:
            return headA
        headA = headA.next
        headB = headB.next

    return None


# Optimal Approach | TC = O ( 2 * max (N, M) ) | SC = O(1)
def getIntersectionPresent(headA, headB):
    d1 = headA
    d2 = headB

    while d1 != d2:
        if d1 is None:
            d1 = headB
        else:
            d2 = d1.next
        
        if d2 is None:
            d2 = headA
        else:
            d2 = d2.next

    return d1