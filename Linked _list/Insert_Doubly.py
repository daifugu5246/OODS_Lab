#Doubly Linked list
class Node:
  def __init__(self,data = None):
    self.data = data
    self.next = None
    self.previous = None

  def __str__(self):
    return self.data

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
      new_node.previous = self.tail
      self.tail = self.tail.next
      
  def addBefore(self,data):
    new_node = Node(data)
    if self.head != None:
      self.size += 1
      new_node.next = self.head
      self.head.previous = new_node
      self.head = new_node
    else:
      self.size += 1
      self.head = new_node
      self.tail = self.head
    while self.tail != None and self.tail.next != None:
        self.tail = self.tail.next
      
  def insert(self,index,data):
    new_node = Node(data)
    pos = self.head
    prev = None
    if index >= 0 and index <= self.size:
      for i in range(index):
        prev = pos
        pos = pos.next
      if prev == None:
        new_node.next = self.head
        if self.head != None:
          self.head.previous = new_node
        self.head = new_node
        self.tail =self.head
        self.size += 1
        print(f'index = {index} and data = {data}')
      else:
        prev.next = new_node
        new_node.previous = prev
        new_node.next = pos
        if pos != None:
          pos.previous = new_node
        self.size += 1
        print(f'index = {index} and data = {data}')
      while self.tail != None and self.tail.next != None:
        self.tail = self.tail.next
    else:
      print('Data cannot be added')
      
  def str_reverse(self):
    print_node = self.tail
    s = ''
    while print_node != None:
      s += str(print_node)
      if print_node.previous != None:
        s += '->'
      print_node = print_node.previous
    return s

  def remove(self,data):
    dummy = Node()
    dummy.next = self.head
    temp = dummy.next
    index = 0
    while self.size != 0 and temp.data != data:
      temp = temp.next
      index += 1
    else:
      if temp != None:
        prev = temp.previous
        next = temp.next
        if prev != None:
          prev.next = next
        else:
          self.head = None
        if next != None:
          next.previous = prev
        else:
          self.tail = None
        if index == 0:
          self.head = next
        print(f'removed : {data} from index : {index}')
        self.size -= 1
      else:
         print('Not Found!')
    return temp
       
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
list = Linked_list()

for  element in inp:
  order = element.split()[0]
  value = element.split()[1]
  if order == 'A':
    list.append(value)
    print('linked list :', list)
    print('reverse :', list.str_reverse())
  elif order == 'Ab':
    list.addBefore(value)
    print('linked list :', list)
    print('reverse :', list.str_reverse())
  elif order == 'I':
    index = value.split(':')[0]
    data = value.split(':')[1]
    list.insert(int(index),data)
    print('linked list :', list)
    print('reverse :', list.str_reverse())
  elif order == 'R':
    list.remove(value)
    print('linked list :', list)
    print('reverse :', list.str_reverse())
  else:
    print('Order is unknown')