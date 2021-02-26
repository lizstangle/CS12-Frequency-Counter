from Node import Node

class LinkedList:

  def __init__(self):
    self.head = None


  def append(self, new_data):
    new_node = Node(new_data)
    new_node.next = self.head
    self.head = new_node

# starts at head, keeps track of whether it's found. counter returns index. when updating we don't need a counter,.node to node from head and stops if finds = to none

  def find(self,item):

    current = self.head

    found = False
    counter = 0

    while current != None and not found:

      if current.data[0] == item:
        found = True
      else:
        current = current.next
        counter += 1

    if found:
      return counter
    else:
      return -1

  # this method will find the key in hte linked list and it will increment it's value by 1
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
  def update2(self,key, value):

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
        
        # we would look for the item and go trhough each element of the node, in this case a linked list, compare and stop when mathed


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
        # chalnge below
        print(f'Node {i}: {current.data}')
        current = current.next