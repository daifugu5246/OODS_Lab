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
    s = str(self.list)
    return s

def isMatch(a,b):
  open_par = '[{('
  close_par = ']})'
  return open_par.index(a) == close_par.index(b)

def parenMatching(paren):
  s = Stack()
  for i in range(len(paren)):
    if paren[i] in '[{(':
      s.push(paren[i])
    elif paren[i] in ']})':
      if not s.isEmpty() and s.peek() in '[{(':
        temp = s.peek()
        s.push(paren[i])
        if isMatch(temp,paren[i]):
          s.pop()
          s.pop()
      else:
        s.push(paren[i])
  else:
    have_open = None
    have_close = None
    for i in s.list:
      if i in '[{(':
        have_open = True
      elif i in ']})':
        have_close = True
    
    if have_open and have_close:
      print('unmatch')
    elif have_open and not have_close:
      print('open excess')
    elif have_close and not have_open:
      print('close excess')
    elif not have_open and not have_close:
      print('match')


inp = input('Enter input : ')
parenMatching(inp)
