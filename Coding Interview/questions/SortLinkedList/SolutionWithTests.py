# Template for linked list node class
class LinkedListNode:
    # __init__ will be used to make a LinkedListNode type object.
    def __init__(self, data, next=None):
        self.data = data
        self.next = next

def merge_two_sorted_lists(l1, l2):
    dummy = LinkedListNode(0)
    tail = dummy
    
    while l1 and l2:
        if l1.data < l2.data:
            tail.next = l1
            l1 = l1.next
        else:
            tail.next = l2
            l2 = l2.next
        tail = tail.next
    
    if l1:
        tail.next = l1
    if l2:
        tail.next = l2
        
    return dummy.next

def find_middle(head):
    slow, fast = head, head
    prev = None
    while fast and fast.next:
        prev = slow
        slow = slow.next
        fast = fast.next.next
    if prev:
        prev.next = None  # Split the list into two halves
    return slow

def sort_list(head):
    if not head or not head.next:
        return head
    
    mid = find_middle(head)
    left = sort_list(head)
    right = sort_list(mid)
    
    return merge_two_sorted_lists(left, right)

# Helper function to create a linked list from a list
def create_linked_list(arr):
    dummy = LinkedListNode(0)
    current = dummy
    for val in arr:
        current.next = LinkedListNode(val)
        current = current.next
    return dummy.next

# Helper function to print the linked list
def print_linked_list(head):
    while head:
        print(head.data, end=" -> ")
        head = head.next
    print("None")

# Example usage:
arr = [4, 2, 1, 3]
head = create_linked_list(arr)
print("Original Linked List:")
print_linked_list(head)

sorted_head = sort_list(head)
print("Sorted Linked List:")
print_linked_list(sorted_head)
