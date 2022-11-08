#Singly Linked list
class Node:
  def __init__(self,data = None):
    self.data = data
    self.next = None

  def __str__(self):
    return str(self.data)

class Linked_list:
  def __init__(self):
    self.head = None
    self.tail = None
    self.size = 0

  def append(self,data):
    new_node = Node(data)
    if self.head == None:
      self.size += 1
      self.head = new_node
      self.tail = self.head
    else:
      self.size += 1
      self.tail.next = new_node
      self.tail = self.tail.next

  def insert(self,index,data):
    new_node = Node(data)
    pos = self.head
    prev = None
    if index >= 0:
      for i in range(index):
        prev = pos
        pos = pos.next
      if prev == None:
        new_node.next = self.head
        self.head = new_node
        self.size += 1
      else:
        prev.next = new_node
        new_node.next = pos
        self.size += 1
      while self.tail != None and self.tail.next != None:
        self.tail = self.tail.next
    else:
      for i in range(self.size+index):
         prev = pos
         pos = pos.next
      if prev == None:
        new_node.next = self.head
        self.head = new_node
        self.size += 1
      else:
        prev.next = new_node
        new_node.next = pos
        self.size += 1
      while self.tail != None and self.tail.next != None:
        self.tail = self.tail.next

  def isEmtpy(self):
    return self.head == None

  def __len__(self):
    return self.size
  
  def __str__(self):
    print_node = self.head
    s = ''
    while print_node != None:
      s += str(print_node)
      if print_node.next != None:
        s += '->'
      print_node = print_node.next
      
    return s


inp = input('Enter Input : ').split(',')
list = inp.pop(0).split()
l_list = Linked_list()

for i in list:
  l_list.append(int(i))

if l_list.isEmtpy():
  print('List is empty')
else:
  print('link list :',l_list)

for data in inp:
  temp = data.split()[0].split(':')
  if int(temp[0]) >= 0 and int(temp[0]) <= l_list.size :
    l_list.insert(int(temp[0]),int(temp[1]))
    print(f'index = {temp[0]} and data = {temp[1]}')
  else:
    print('Data cannot be added')
  
  if l_list.isEmtpy():
    print('List is empty')
  else:
    print('link list :',l_list)

