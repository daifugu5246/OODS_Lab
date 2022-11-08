'''ให้น้องๆเขียนโปรแกรมโดยรับ input 2 แบบ โดยใช้ Queue ในการแก้ปัญหา



E  <value>  ให้นำ value ไปใส่ใน Queue และทำการแสดงผล ข้อมูลปัจจุบันของ Queue

D                 ให้ทำการ Dequeue ตัวที่อยู่หน้าสุดของ Queue ออก หลังจากนั้นแสดงตัวเลขที่เอาออกมา และ แสดงผลข้อมูล
                    ปัจจุบันของ Queue

***และเมื่อจบการทำงานให้แสดงผลข้อมูลปัจจุบันของ Queue พร้อมกับข้อมูลที่ถูก Dequeue ทั้งหมดตามลำดับ
***ถ้าหากไม่มีข้อมูลใน Queue แล้วให้แสดงคำว่า  Empty'''
class Queue:
  def __init__(self,L=None):
    if L == None:
      self.list = []
    else:
      self.list = L

  def enQueue(self,data):
    self.list.append(data)

  def deQueue(self):
    return self.list.pop(0)

  def isEmpty(self):
    return self.list == []

  def size(self):
    return len(self.list)
  
  def __str__(self):
    s = ''
    for data in self.list:
      s += str(data) + ', '
    else:
      s = s[:-2]
    if s == '':
      s = 'Empty'
    return s


user_input = input('Enter Input : ').split(',')
q = Queue()
dq = Queue()
for i in user_input:
  temp_list = i.split()
  if temp_list[0] == 'E':
    q.enQueue(int(temp_list[1]))
    print(q)
  elif temp_list[0] == 'D':
    if not q.isEmpty():
      temp = q.deQueue()
      dq.enQueue(temp)
      print(temp,'<-',q)
    else:
      print(q)

print(dq,':',q)
