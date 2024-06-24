class ListNode:
    def __init__(self, val, next_node = None):
        self.val = val
        self.next = next_node

    
    def print_linkedlist(self):
        temp = self
        while temp is not None:
            print(temp.val, end = ' ')
            temp = temp.next
        print()


    def length_linkedlist(self):
        temp = self
        count = 0
        while temp is not None:
            count += 1
            temp = temp.next

        return count