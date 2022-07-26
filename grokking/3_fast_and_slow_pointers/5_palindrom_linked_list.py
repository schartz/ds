class Node:  
    def __init__(self, val, next=None):    
        self.val = val    
        self.next = next

def print_list(head):
    s = ''
    h = head
    while h:
        s = s + '-->' + str(h.val)
        h = h.next
    print(s)


def is_palindromic_linked_list(head):
    slow = fast = head
    middle = None
    is_palindrome = True


    while fast is not None and fast.next is not None:
        fast = fast.next.next
        slow = slow.next

    fast = head


    reversed_mid = reversed(slow)
    mid = reversed_mid
    

    while reversed_mid is not None:
        if reversed_mid.val != fast.val:
            is_palindrome = False
            break
        reversed_mid = reversed_mid.next
        fast = fast.next

    reversed(mid)
    
    print_list(head)
    print_list(mid)
    print('--------')
    return is_palindrome


def reversed(head):
    previous = None
    current = head

    while current is not None:
        tmp = current.next
        current.next = previous
        previous = current
        current = tmp
    return previous

# 1 2 4 6 4 2 1

# malayalam

# racecar

def main():  
    head = Node(2)  
    head.next = Node(4)  
    head.next.next = Node(6)  
    head.next.next.next = Node(4)  
    head.next.next.next.next = Node(2)

    print_list(head)
    print('======')
    print("Is palindrome: " + str(is_palindromic_linked_list(head)))
    print_list(head)

    head.next.next.next.next.next = Node(2)
    print("Is palindrome: " + str(is_palindromic_linked_list(head)))

main()