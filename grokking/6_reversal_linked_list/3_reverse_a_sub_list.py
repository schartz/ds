class Node:  
    def __init__(self, value, next=None):    
        self.val = value    
        self.next = next

    def __repr__(self):
    	return str(self.val)


    def print_list(self):
        temp = self
        while temp is not None:
            print(f'{temp.val}-->', end=" ")
            temp = temp.next
        print()


def reverse_ranged(head, p, q):
	n = 1
	current = head
	start = end = reversal_head = None

	while current:
		n += 1
		if n == p:
			start = current
		current = current.next
		if n == p:
			reversal_head = current
		if n == q:
			end = current.next

	reversed_head, reversed_tail = reverse(reversal_head, q-p+1)

	start.next = reversed_head
	reversed_tail.next = end
	return head




def reverse(head, steps):

	current = head
	previous = None
	count = 1 

	while current and count < steps + 1:

		tmp = current.next
		current.next = previous
		previous = current
		current = tmp
		count +=1

	tail = previous
	while tail.next:
		tail = tail.next
	previous.print_list()

	return previous, tail


def main():  
    head = Node(1)
    head.next = Node(2)
    head.next.next = Node(3)
    head.next.next.next = Node(4)
    head.next.next.next.next = Node(5)

    print("Nodes of original LinkedList are: ", end='')
    head.print_list()
    result = reverse_ranged(head, 2, 4)
    print("Nodes of reversed LinkedList are: ", end='')
    result.print_list()

main()