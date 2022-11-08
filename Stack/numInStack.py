'''จงสร้างฟังก์ชัน ManageStack() ในการจัดการตัวเลขที่อยู่ใน Stack โดยที่จะมีคำสั่งดังนี้

A (add) : ทำการเพิ่มตัวเลขเข้าไปใน Stack

P (pop) : ทำการนำเลขสุดท้ายใน Stack ออก ( ถ้า Stack ว่างให้แสดงผล -1 )

D (delete) : ทำการลบตัวเลขที่ต้องการใน Stack ( ถ้า Stack ว่างให้แสดงผล -1 )  

LD (lessthan delete) : ทำการลบตัวเลขที่น้อยกว่าตัวเลขที่กำหนดทั้งหมดออกจาก Stack และแสดงผลตัวเลขที่ถูกลบไป ( ถ้า Stack ว่างให้แสดงผล -1 )

MD (Morethan delete) : ทำการลบตัวเลขที่มากกว่าตัวเลขที่ต้องการทั้งหมดออกจาก Stack และแสดงผลตัวเลขที่ถูกลบไป ( ถ้า Stack ว่างให้แสดงผล -1 )

การ Delete ทุกแบบ ถ้าหากไม่มีเลขที่ถูกลบเลย ไม่ต้องแสดงผลอะไรและให้ทำการแสดงผลค่าที่อยู่ใน Stack เมื่อจบโปรแกรม

*** Hint ***

ฟังก์ชัน Delete ต่างๆให้สร้าง Stack ขึ้นมาอีก 1 อันเพื่อใช้เป็น Temp ในการเก็บค่าตัวเลขต่างๆ'''
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

def ManageStack(x):
  s = Stack()
  temp = Stack()
  list = x.split(',')
  for i in list:
    #Add
    if i.split()[0] == 'A':
      s.push(int(i.split()[1]))
      print('Add =',i.split()[1])
    #Pop
    elif i.split()[0] == 'P':
      if s.isEmpty():
        print(-1)
      else:
        print('Pop =',s.pop())
    #Delete
    elif i.split()[0] == 'D':
      if s.isEmpty():
        print(-1)
      else:
        while not s.isEmpty():
          if s.peek() == int(i.split()[1]) :
            print('Delete =',s.peek())
            s.pop()
          else:
            temp.push(s.peek())
            s.pop()
        while not temp.isEmpty():
          s.push(temp.peek())
          temp.pop()
    #MoreDelete 
    elif i.split()[0] == 'MD':
      if s.isEmpty():
        print(-1)
      else:
        while not s.isEmpty():
          if s.peek() > int(i.split()[1]):
            print('Delete =',s.peek(),'Because',s.peek(),'is more than',int(i.split()[1]))
            s.pop()
          else:
            temp.push(s.peek())
            s.pop()
        while not temp.isEmpty():
          s.push(temp.peek())
          temp.pop()
    #LessDelete
    elif i.split()[0] == 'LD':
     if s.isEmpty():
        print(-1)
     else:
        while not s.isEmpty():
          if s.peek() < int(i.split()[1]):
            print('Delete =',s.peek(),'Because',s.peek(),'is less than',int(i.split()[1]))
            s.pop()
          else:
            temp.push(s.peek())
            s.pop()
        while not temp.isEmpty():
          s.push(temp.peek())
          temp.pop()
    else:
      pass
  return s

user_input = input('Enter Input : ')
print(ManageStack(user_input))  
  
