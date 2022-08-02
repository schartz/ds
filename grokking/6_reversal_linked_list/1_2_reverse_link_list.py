class Node:  
    def __init__(self, value, next=None):    
        self.val = value    
        self.next = next


    def print_list(self):
        temp = self
        while temp is not None:
            print(f'{temp.val}-->', end=" ")
            temp = temp.next
        print()


def reverse(head):
    current = head
    previous = None
    while current:
        tmp = current.next
        current.next = previous
        previous = current
        current = tmp
    return previous
    


def main():  
    head = Node(2)
    head.next = Node(4)
    head.next.next = Node(6)
    head.next.next.next = Node(8)
    head.next.next.next.next = Node(10)

    print("Nodes of original LinkedList are: ", end='')
    head.print_list()
    result = reverse(head)
    print("Nodes of reversed LinkedList are: ", end='')
    result.print_list()

main()