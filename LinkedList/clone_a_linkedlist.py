from linkedlist import ListNode


# TC - O(2N) Space - O(N) + O(N)
def copyRandomList(head:ListNode)->ListNode:
    temp = head

    mpp = {}


    while temp is not None:
        newNode = ListNode(temp.val)

        mpp[temp] = newNode

        temp = temp.next


    temp = head


    while temp is not None:

        copyNode = mpp[temp]


        copyNode.next = mpp.get(temp.next, None)

        copyNode.random = mpp.get(temp.random, None)

        temp = temp.next




    return mpp[head]