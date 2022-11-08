#Singly Linked list
class Node:
  def __init__(self,data = None):
    self.data = data
    self.next = None

class Linked_list:
  def __init__(self):
    self.head = None
    self.current = None

  def append(self,data):
    new_node = Node(data)
    if self.head == None:
      self.head = new_node
      self.current = self.head
      self.head.next  = None
      self.head.index = 0
    else:
      self.current.next = new_node
      self.current = self.current.next
      self.current.next = None

  def insert(self,index,data):
    new_node = Node(data)
    pos = self.head
    prev = None
    for i in range(index):
      prev = pos
      pos = pos.next
    if prev == None:
      new_node.next = self.head
      self.head = new_node
    else:
      prev.next = new_node
      new_node.next = pos
      
  def isEmtpy(self):
    return self.head == None
    
  def __str__(self):
    print_node = self.head
    s = ''
    while print_node != None:
      s += str(print_node.data)
      if print_node.next != None:
        s += '->'
      print_node = print_node.next
      
    return s


l_list = Linked_list()

for i in range(5):
  l_list.append(i) # add data to at the last position of link list


print(l_list) #print data in linked list
l_list.insert(0,20)# insert data at specify index
print(l_list)