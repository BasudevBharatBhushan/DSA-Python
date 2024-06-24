from linkedlist import ListNode



# Brute Force Approach [Time Limit Exceeded] - O(n*k)
def rotateRight(head:ListNode , k:int):

    if head is None or head.next is None:
        return head

    for i in range(k):
        temp = head

        # Go till the 2nd last node
        while temp.next.next is not None:
            temp = temp.next

        end = temp.next
        temp.next = None

        end.next = head

        head = end


    return head

# Optimal Approach

def rotateRight_optimal(head:ListNode, k:int):

    #len = ListNode.length_linkedlist(head)

    # Calculate the length

    temp = head
    length = 1

    while temp.next is not None:
        temp = temp.next
        length +=1

    # Make the linkedlist circular
    temp.next = head

    k = k % length

    end  = length - k

    while end:
        temp = temp.next
        end -=1


    head = temp.next
    temp.next = None


    return head

    




# Test Cases
head = ListNode(1)
head.next = ListNode(2)
head.next.next = ListNode(3)
head.next.next.next = ListNode(4)
head.next.next.next.next = ListNode(5)

ListNode.print_linkedlist(rotateRight(head, 2)) # 4 -> 5 -> 1 -> 2 -> 3 -> None