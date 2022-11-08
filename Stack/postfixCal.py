'''รับ string มาเข้าคิวหา secret code โดยรับ input คือ

code เป็น string ยาว

hint คือตัวแรกของรหัสที่ถูกต้อง



**คำใบ้**

ascii ของ "f" มีค่า = 102

ascii ของ "g" มีค่า = 103

ascii ของ "h" มีค่า = 104

ascii ของ "i" มีค่า = 105

ascii ของ "j" มีค่า = 106'''

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
    
  def isEmpty(self):
    return len(self.list) == 0

  def size(self):
    return len(self.list)

      
def postFixeval(st):
    s = Stack()
    for data in st:
      if isOperator(data):
        if data == '+':
          a = s.pop()
          b = s.pop()
          temp = b + a
          s.push(temp)
        elif data == '-':
          a = s.pop()
          b = s.pop()
          temp = b - a
          s.push(temp)
        elif data == '*':
          a = s.pop()
          b = s.pop()
          temp = b * a
          s.push(temp)
        elif data == '/':
          a = s.pop()
          b = s.pop()
          temp = b / a
          s.push(temp)
        else:
          pass
      else:
        s.push(int(data))

    return s.pop()

def isOperator(op):
  operators = ['+','-','*','/']
  for opr in operators:
    if op == opr:
      x = True
      break
    else:
      x = False
  return x
  
            


print(" ***Postfix expression calcuation***")

token = list(input("Enter Postfix expression : ").split())


print("Answer : ",'{:.2f}'.format(postFixeval(token)))
