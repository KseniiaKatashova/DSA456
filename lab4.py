from typing import List, Any

class SinglyLinkedList:
    class Node:
        def __init__(self, data, next_node=None):
            self.data = data
            self.next = next_node

    def __init__(self):
        self.front = None

    def is_empty(self):
        return self.front is None

    def prepend(self, data):
        nn = SinglyLinkedList.Node(data)
        nn.next = self.front
        self.front = nn
            

    def append(self, data):
        nn = SinglyLinkedList.Node(data)
        if self.front is None:
            self.front = nn
            return
        current = self.front
        while current.next is not None:
            current = current.next
        current.next = nn

    def insert_after(self, target, data): 
        if self.front is None:
            print("The linked list is empty.Can not insert new node after the target node.")
            return
        else:
            nn = SinglyLinkedList.Node(data)
            nn.next = target.next
            target.next = nn
            print("New node inserted.")
            
    def delete(self, target):
        #if the first node is what we are looking for
        if self.front == target:
            self.front = target.next
            del target
            return True
        
        # find the node before the target node
        current = self.front
        while current is not None and current.next is not target:
            current = current.next
        
        # check if the target node was found
        if current is None:
            return False
        
        # delete the target node
        current.next = target.next
        del target
        return True
            

    def search(self, data):
        if self.front is None:
            return "The linked list is empty.No nodes to search."
       
        current = self.front
        while current is not None:
            #The node's data matches what we are looking for
            if current.data == data:
                return current
            else:
                current = current.next
        return None


    def size(self):
        size = 0 
        if self.front is None:          
            print("The linked list is empty")
            return size
        
        current = self.front
        while current is not None:
            size +=1
            current = current.next
        return size


    def to_list(self) -> List[Any]:
        lst = []
        current = self.front
        while current is not None:
            lst.append(current.data)
            current = current.next
        return lst
 
    def print(self):
        current = self.front
        while current is not None:
            print(current.data)
            current = current.next

                        

#Testing
# my_list = SinglyLinkedList()
# my_list.prepend(5)
# my_list.prepend(12)
# my_list.append(10)
# our_list = my_list.to_list()
# print(our_list)
# my_list.size()


