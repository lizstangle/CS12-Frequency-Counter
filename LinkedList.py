from Node import Node

class LinkedList:

  def __init__(self):
    self.head = None

  # append function puts the value pair into a node of a linked list
  def append(self, new_data):
    new_node = Node(new_data)
    new_node.next = self.head
    self.head = new_node

# Starts at head, keeps track of whether word is found. Counter returns index. 

  def find(self,item):

    current = self.head

    found = False
    counter = 0

    while current != None and not found:
      # [0] or "data" is referring to the first element of the tuple which is the key or the word
      if current.data[0] == item:
        found = True
      # if not found look at the next element 
      else:
        current = current.next
        counter += 1

    if found:
      return counter
    else:
      return -1

  # this method will find the key in the linked list and it will increment it's value by 1
  def update(self, key, value):

    current = self.head

    found = False
    counter = 0

    while current != None and not found:

      if current.data[0] == key:
        current.data = (current.data[0], current.data[1]+1)
      else:
        current = current.next
        counter += 1

# 2nd update function
  def update2(self, key, value):

# start at beginning
    current = self.head

    found = False

    while current != None and not found:

      if current.data[0] == key:
        found = True
        new_tuple = (key, current.data[1]+1)
        current.data = new_tuple
        
      else:
        current = current.next

  def length(self):
    if self.head == None:
      return 0
    else:
      counter = 1
      current = self.head
      while(current.next):
        current = current.next
        counter +=1
      return counter


  def print_nodes(self):
    current = self.head
    
    if current == None:
      print('The linked list is empty.')
    else:
      for i in range(self.length()):
        # change below
        # node number that prints is a counter on a particular linked list
        print(f'Node {i}: {current.data}')
        current = current.next