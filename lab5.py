Lab 5 Part B: big-O analysis								
													
1.)													
	def is_empty(self):												
	        return self.front is None						1						
							T(n) = 1						
							O(1)		The time complexity of this function is O(1), which means that it takes constant time to execute, regardless of the size of the input or any other external factors. 				
													
													
2.)													
	def prepend(self, data):												
	        nn = SinglyLinkedList.Node(data)						1						
	        nn.next = self.front						1						
	        self.front = nn						1						
													
							T(n) = 3						
							O(1)						
													
													
3.)													
	def append(self, data):												
	        nn = SinglyLinkedList.Node(data)						1						
	        if self.front is None:						1						
	            self.front = nn												
	            return												
	        current = self.front						1						
	        while current.next is not None:						n						
	            current = current.next						n						
	        current.next = nn						1						
							T(n) = 4+2n						
							O(n)		O(n), where n is the number of nodes currently in the linked list. This is because in the worst case, the method has to traverse the entire linked list to find the last node, which takes a linear amount of time proportional to the size of the linked list.				
													
													
4.)													
	def insert_after(self, target, data): 												
	        if self.front is None:						1						
	            print("The linked list is empty.")												
	            return												
	        else:												
	            nn = SinglyLinkedList.Node(data)						1						
	            nn.next = target.next						1						
	            target.next = nn						1						
	            return print("New node inserted.")						1						
							T(n)=5						
							O(1)						
													
													
5.)													
	def delete(self, target):												
	     												
	        if self.front == target:									1			
	            self.front = target.next												
	            del target												
	            return True												
													
	 												
	        current = self.front									1			
	        while current is not None and current.next is not target:									2+n			
	            current = current.next									n+1			
	        												
	   												
	        if current is None:												
	            return False												
	        												
	 												
	        current.next = target.next									1			
	        del target									1			
	        return True									1			
										T(n)= 8 +2n			
										O(n)			
													
6.)													
	def search(self, data):												
	        if self.front is None:									1			
	            return "The linked list is empty.No nodes to search."												
	       												
	        current = self.front									1			
	        while current is not None:									n			
	        												
	            if current.data == data:									1+n			
	                return current									1			
	            else:												
	                current = current.next									1			
	        return None									1			
										T(n)=6 +2n			
										O(n)			
													
7.)													
	def size(self):												
	        size = 0 												
	        if self.front is None:          							1					
	            print("The linked list is empty")												
	            return size												
	        												
	        current = self.front							1					
	        while current is not None:							n					
	            size +=1							n+1					
	            current = current.next							n+1					
	        return size							1					
								T(n)=5+3n					
								O(n)					
													
8.)													
	 def to_list(self) -> List[Any]:												
	        lst = []							1					
	        current = self.front							1					
	        while current is not None:							n					
	            lst.append(current.data)							1+n					
	            current = current.next							1+n					
	        return lst							1					
								T(n)=5+3n					
								O(n)					
													
													
9.)													
	def print(self):												
	        current = self.front							1					
	        while current is not None:							n					
	            print(current.data)							1+n					
	            current = current.next							1+n					
								T(n)=3+3n					
								O(n) 					
