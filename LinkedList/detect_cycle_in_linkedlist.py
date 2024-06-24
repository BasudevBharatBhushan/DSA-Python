from linkedlist import ListNode

# Set Method | TC - O(N2logN)
def hasCycle_set(head:ListNode)->bool:
    st = set()

    while head is not None:
        if head in st:
            return True
        
        st.add(head)

        head = head.next


# Tortoise and Hare Method

def hasCycle_tortoise_n_hare(head:ListNode)->bool:
    slow = head
    fast = head

    while fast is not None and fast.next is not None:
        slow = slow.next
        fast = fast.next.next

        if slow is fast:
            return True
        
        head = head.next

        return False
    


#Test Cases