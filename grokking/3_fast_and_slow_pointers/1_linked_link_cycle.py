# Given the head of a Singly LinkedList, write a function to 
# determine if the LinkedList has a cycle in it or not.

import time


def print_execution_time(func, *args, **kwargs):
    def wrapper(*args, **kwargs):
        ts = time.time()
        _ = func(*args, **kwargs)
        print(f'Execution time {time.time() - ts}')
        return _
    return wrapper


class Node:  
    def __init__(self, value, next=None):    
        self.val = value    
        self.next = next


def has_cycle(head):
    if head == None:
            return False
        
    slow_pointer, fast_pointer = head, head.next
    
    while slow_pointer != fast_pointer:
        if fast_pointer == None or fast_pointer.next == None:
            return False

        slow_pointer = slow_pointer.next
        fast_pointer = fast_pointer.next.next

    return True


def has_cycle2(head):
    if head == None:
            return False
        
    slow_pointer, fast_pointer = head, head

    while fast_pointer and fast_pointer.next:
        slow_pointer = slow_pointer.next
        fast_pointer = fast_pointer.next.next

        if slow_pointer == fast_pointer:
            return True

    return False




def main():
    head = Node(1)
    head.next = Node(2)
    head.next.next = Node(3)
    head.next.next.next = Node(4)
    head.next.next.next.next = Node(5)
    head.next.next.next.next.next = Node(6)
    print("LinkedList has cycle: " + str(has_cycle(head)))   
    head.next.next.next.next.next.next = head.next.next  
    print("LinkedList has cycle: " + str(has_cycle(head)))   
    head.next.next.next.next.next.next = head.next.next.next  
    print("LinkedList has cycle: " + str(has_cycle(head)))  

main()