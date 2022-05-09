class Node():
    def __init__(self, data: int):
        self.item = data
        self.next = None


class LinkedList():
    size = 0
    def __init__(self, node: Node):
        self.head = node
        self.size += 1


    def list_append(self, node: Node):
        current = self.head
        while current.next is not None:
            current = current.next
        current.next = node
        self.size += 1


    def add_to_front(self, node:Node):
        node.next = self.head 
        self.head = node
        self.size += 1


    def delete_tail(self):

        if self.head.next == None:
            self.head = None

        current = self.head

        while current.next.next is not None:
            current = current.next

        # for i in range(1, self.size-1):
        #     current = current.next

        current.next = None
        self.size-=1


    def delete_head(self):
        self.head = self.head.next 
        self.size-=1  



    def delete(self, idx):
        if idx > self.size or idx < 0:
            raise ValueError

        if idx == 1:
            self.delete_head() 
            return 

        if idx == self.size:
            self.delete_tail()  
            return   

        
        counter = 1
        current = self.head

        while counter < idx-1:
            print(f'{counter} {idx}')
            current = current.next
            counter+=1

        current.next = current.next.next 

        self.size-=1   



    def add(self, node:Node, idx:int):

        if idx == 1:
            self.add_to_front(node)
            return 

        if idx == self.size:
            self.list_append(node)
            return

        
        if idx > self.size or idx<0:
            raise ValueError

        
        counter = 1
        current = self.head

        while counter < idx-1:
            current = current.next
            counter+=1
            
        node.next = current.next
        current.next = node 

        self.size+=1   



    def show(self):
        current = self.head
        while current is not None:
            print(current.item)
            current = current.next
        print()
        print('-------')


# n1 = Node(10)
# n2 = Node(20)
# n3 = Node(30)

# head = Node(10)
# head.next = Node(20)
# n2.next = n3

# current = head
# while current is not None:
#   print(current.item)
#   current = current.next

myll = LinkedList(Node(55))
myll.list_append(Node(66))
myll.list_append(Node(78))
myll.list_append(Node(68))
myll.list_append(Node(88))

myll.show()

print(myll.size)

print('**************')

myll.add(Node(58), 2)

myll.show()