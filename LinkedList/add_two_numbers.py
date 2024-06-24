from linkedlist import ListNode

# Brute Froce Apparoch | TC = O(N1+N2) | SC = O(N1+N2)
def add_two_numbers(l1:ListNode, l2:ListNode)->ListNode:

    temp1 = l1
    temp2 = l2
    prev1 = None
    prev2 = None

    result_node = ListNode(-1)

    num1 = 0
    num2 = 0
    res = 0


    # Reverse l1
    while temp1 is not None:
        front = temp1.next
        temp1.next = prev1

        prev1 = temp1

        temp1 = front

    # Reverse l2
    while temp2 is not None:
        front = temp2.next
        temp2.next = prev2

        prev2 = temp2

        temp2 = front
    
    # ListNode.print_linkedlist(prev1)
    # ListNode.print_linkedlist(prev2)

    # Store l1 into num1
    while prev1 is not None:
        num1=(num1*10)+prev1.val

        prev1 = prev1.next

    # Store l2 into num2
    while prev2 is not None:
        num2 = (num2*10)+prev2.val

        prev2 = prev2.next

    # print(num1, num2)

    res = num1+num2


    res = str(res)

    res = res[::-1]

    result_node_head = result_node

    for char in res:
        result_node.next = ListNode(int(char))
        result_node = result_node.next
 
     

    
    return result_node_head.next


# Optimal Approach | Elementary Math
"""
2 4 3 
5 6 4
----------------


"""
def add_two_numbers_optimal(l1:ListNode, l2:ListNode)->ListNode:
    result_node = ListNode(-1)
    head = result_node
    carry = 0
    sum = 0

    while (l1 is not None or l2 is not None) or carry:
        sum = 0

        if l1 is not None:
            sum += l1.val
            l1 = l1.next
        
        if l2 is not None:
            sum += l2.val
            l2 = l2.next

        sum += carry

        carry = sum // 10

        node = ListNode(sum % 10)

        result_node.next = node

        result_node = result_node.next

    return head.next
        


    # Check if last carry is two digit



    # Two more edge cases needs to be handled like...
    """
    1. If last carry will be a two digit number

    2. When uneuql length of linkedlist are getting added


    2 4 9
    5 6 9
    ---------
    7 0 9 1
    ..........................

    2 4 9 9
    5 6 9
    --------------
    7 0 9 0 1

    """
            
        
"""
Dry Run

Input:
  l1: 2 -> 4 -> 9
  l2: 5 -> 6 -> 9

Iteration 1:
  l1: 2 -> 4 -> 9
  l2: 5 -> 6 -> 9
  |
  v
  carry = 0, sum = 2 + 5 = 7
  result_node: -1 -> 7
  result_node: -1 -> 7 -> 
  carry = 0

Iteration 2:
  l1: 4 -> 9
  l2: 6 -> 9
       |
       v
  carry = 0, sum = 4 + 6 = 10
  result_node: -1 -> 7 -> 0
  result_node: -1 -> 7 -> 0 -> 
  carry = 1

Iteration 3:
  l1: 9
  l2: 9
            |
            v
  carry = 1, sum = 9 + 9 + 1 = 19
  result_node: -1 -> 7 -> 0 -> 9
  result_node: -1 -> 7 -> 0 -> 9 -> 
  carry = 1

Iteration 4:
  l1: None
  l2: None
                 |
                 v
  carry = 1, sum = 0 + 0 + 1 = 1
  result_node: -1 -> 7 -> 0 -> 9 -> 1
  result_node: -1 -> 7 -> 0 -> 9 -> 1 -> 

Output:
  7 -> 0 -> 9 -> 1


"""

        
"""


Input:
  l1: 2 -> 4 -> 9 -> 9
  l2: 5 -> 6 -> 9

Iteration 1:
  l1: 2 -> 4 -> 9 -> 9
  l2: 5 -> 6 -> 9
  |
  v
  carry = 0, sum = 2 + 5 = 7
  result_node: -1 -> 7
  result_node: -1 -> 7 -> 
  carry = 0

Iteration 2:
  l1: 4 -> 9 -> 9
  l2: 6 -> 9
       |
       v
  carry = 0, sum = 4 + 6 = 10
  result_node: -1 -> 7 -> 0
  result_node: -1 -> 7 -> 0 -> 
  carry = 1

Iteration 3:
  l1: 9 -> 9
  l2: 9
            |
            v
  carry = 1, sum = 9 + 9 + 1 = 19
  result_node: -1 -> 7 -> 0 -> 9
  result_node: -1 -> 7 -> 0 -> 9 -> 
  carry = 1

Iteration 4:
  l1: 9
  l2: None
                 |
                 v
  carry = 1, sum = 9 + 0 + 1 = 10
  result_node: -1 -> 7 -> 0 -> 9 -> 0
  result_node: -1 -> 7 -> 0 -> 9 -> 0 -> 
  carry = 1

Iteration 5:
  l1: None
  l2: None
                    |
                    v
  carry = 1, sum = 0 + 0 + 1 = 1
  result_node: -1 -> 7 -> 0 -> 9 -> 0 -> 1
  result_node: -1 -> 7 -> 0 -> 9 -> 0 -> 1 -> 

Output:
  7 -> 0 -> 9 -> 0 -> 1


"""


# Test Cases

l1 = ListNode(2)
l1.next = ListNode(4)
l1.next.next = ListNode(3)

l2 = ListNode(5)
l2.next = ListNode(6)
l2.next.next = ListNode(4)


ListNode.print_linkedlist(add_two_numbers_optimal(l1, l2))



