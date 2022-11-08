'''ให้น้องๆเขียนโปรแกรมโดยรับ input 2 แบบ โดยใช้ STACK ในการแก้ปัญหา



A  <value>  ให้นำ value ไปใส่ใน STACK และทำการแสดงผล Size ปัจจุบันของ STACK

P                 ให้ทำการแสดงผลของvalueที่อยู่ท้ายสุดและindexของvalueนั้นจากนั้นทำการ Pop_Stack ถ้าหากไม่มี value อยู่ใน Stack ให้แสดงผลเป็น  -1

*** ในตอนสุดท้ยถ้าหากใน Stack ยังมี Value อยู่ให้แสดงผลออกมา  ถ้าหากไม่มีแล้วให้แสดงคำว่า  Empty'''
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
      s += 'Empty'
    else:
      for data in self.list:
        s += data + ' '
    return s

a = input("Enter Input : ").split(',')
s = Stack()
for i in a:
  if i[0] == 'A':
    temp = i.split()
    s.push(temp[1])
    print('Add = ' + temp[1] + ' and Size = ' + str(s.size()))
  elif i[0] == 'P':
    if s.isEmpty():
       print(-1)
    else:
       print('Pop = ' + s.pop() + ' and Index = ' + str(s.size()))
  else:
    pass
else:
  print(s)
