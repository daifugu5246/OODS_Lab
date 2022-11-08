'''จำลองการเลื่อนแถวคอยภายในเวลาที่กำหนดโดยใช้ class queue

โดยที่มีแถวหลัก 1 แถวยาวกี่คนก็ได้

แถวหน้า cashier 1 ยาว 5 คน โดยที่คนนี้จะใช้เวลา 3 นาทีในการคิดค่าบริการ

แถวหน้า cashier 2 ยาว 5 คน โดยที่คนนี้จะใช้เวลา 2 นาทีในการคิดค่าบริการ

ลูกค้าจะ move แถวทุกๆ 1 นาที โดยหากแถว 1 ว่างจะไปก่อนหากเต็มจึงไปแถว 2

จงแสดง นาที [แถวหลัก] [แถว cashier 1] [แถว cashier 2] จนกว่าแถวหลักจะหมด'''
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
    return str(self.list)

people = input('Enter people : ')
list = []
# list.extend(people)
for char in people:
  if char in '123456789' or char == ' ':
    continue
  else:
    list.append(char)

main_q = Queue(list)
cash_1 = Queue()
cash_2 = Queue()
count_1 = 0
count_2 = 0           
#for i in range(1,main_q.size() + 1):
for i in range(1,len(people)):
  
  if cash_1.size() < 5 and not main_q.isEmpty():
    tmp_1 = main_q.deQueue()
    cash_1.enQueue(tmp_1)
    count_1 += 1
    if not cash_2.isEmpty():
      count_2 += 1
  elif cash_1.size() >= 5 and not main_q.isEmpty():
    count_1 += 1
    if cash_2.size() < 5:
      tmp_2 = main_q.deQueue()
      cash_2.enQueue(tmp_2)
      count_2 +=1
    elif cash_2.size() >= 5:
      count_2 += 1
     
  print(i,main_q,cash_1,cash_2)
  
  if count_1 == 3 and not cash_1.isEmpty():
    cash_1.deQueue()
    count_1 = 0
    
  if count_2 % 2 == 0 and not cash_2.isEmpty():
    cash_2.deQueue()
