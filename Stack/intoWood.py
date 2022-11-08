class Stack:
  def __init__(self,L=None):
    if L == None:
      self.list = []
    else:
      self.list = L
    
  def pop(self):
    return self.list.pop()

  def push(self,i):
    self.list.append(i)

  def peek(self):
    return self.list[-1]
  
  def isEmpty(self):
    return len(self.list) == 0

  def size(self):
    return len(self.list)
    
  def __str__(self):
    s = 'Value in Stack = '
    if self.list == []:
      s += str(self.list)
    else:
      s += str(self.list)
    return s

    
S = Stack()
temp = Stack()
count = 0
inp = input('Enter Input : ').split(',')
for i in inp:
  a = i.split()
  if a[0] == 'A':
    S.push(int(a[1]))
  elif a[0] == 'B':
    if S.isEmpty():
      pass
    else:
      temp.push(S.peek())
      most = S.pop()
      count += 1
    while not S.isEmpty():
      if S.peek() > most:
        most = S.peek()
        temp.push(S.peek())
        S.pop()
        count += 1 
      else:
        temp.push(S.peek())
        S.pop()
    else:
      print(count)
      count = 0
      while not temp.isEmpty():   
        S.push(temp.pop())
      
      
      
    
