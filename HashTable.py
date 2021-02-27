from LinkedList import LinkedList

class HashTable:

  def __init__(self, size):
    self.size = size
    self.arr = self.create_arr(size)


  # 1️⃣ DONE: Complete the create_arr method.

  # Each element of the hash table (arr) is a linked list.
  # This method creates an array (list) of a given size and populates each of its elements with a LinkedList object.

  def create_arr(self, size):
    arr = []

    # every element in the array will be a linked list
    for i in range(size):
      new_ll = LinkedList()
      arr.append(new_ll)

    return arr

  # 2️⃣ DONE: Create your own hash function.

  # Hash functions turn each of the keys into an index value that can be used to determine where in our list each 
  # key:value pair should be stored. 
  
  # Hash function is an efficient way of storing values based on keys - an organzition system or indexing system
  # My hash function will convert a key which is a string into a character into an integer
  def hash_func(self, key):
    index = ord(key[0]) % self.size
    return index
    

  # 3️⃣ TODO: Complete the insert method.

  # Should insert a key value pair into the hash table, where the key is the word and the value is a counter 
  # for the number of times the word appears. When inserting a new word in the hash table, be sure to check 
  # if there is a Node with the same key in the table already.

  def insert(self, key, value):

    new_data = (key, value)

    arr_index = self.hash_func(key)

    ll = self.arr[arr_index]


    # If not found, append
    if  ll.find(key) == -1:
      # print(f"{key} was not found")
      ll.append(new_data)

    else:
      ll.update2(key, value)



  # 4️⃣ DONE: Complete the print_key_values method.

  # Traverse through the every Linked List in the table and print the key value pairs.

  # For example: 
  # a: 1
  # again: 1
  # and: 1
  # blooms: 1
  # erase: 2

  def print_key_values(self):
    
    for ll in self.arr:
      ll.print_nodes()




