""" 
Exercise_3 : Find Mid Point of a Singly Linked List.

# Time Complexity :
- printMiddle(): O(n) where n is number of nodes (traverses list once)
- push(): O(1) constant time operation at head

# Space Complexity :
- O(1) as we only use two pointers of constant size

"""

# Node class  
class Node:  
   # Function to initialise the node object  
   def __init__(self, data):  
       self.data = data
       self.next = None
       
class LinkedList: 
   def __init__(self): 
       self.head = None

   def push(self, new_data): 
       new_node = Node(new_data)
       new_node.next = self.head
       self.head = new_node
 
   # Function to get the middle of  
   # the linked list 
   def printMiddle(self): 
       slow = self.head
       fast = self.head

       while fast and fast.next:
           slow = slow.next
           fast = fast.next.next
        
       print(slow.data if slow else "The list is empty")

# Driver code 
list1 = LinkedList() 
list1.push(5) 
list1.push(4) 
list1.push(2) 
list1.push(3) 
list1.push(1) 
list1.printMiddle()
