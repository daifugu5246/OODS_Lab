'''ที่จอดรถของนาย ก เป็นส่วนที่แรเงาสีฟ้า ส่วนสีแดงเป็นที่ของนาย ข ซี่งเป็นญาติกัน ที่จอดรถของนาย ก และ นาย ข แคบมาก จอดรถได้เรียงเดี่ยว นาย ข ไม่ได้ใช้ที่จอดรถ แต่ อนุญาติให้นาย ก ใช้ที่จอดรถของเขาได้โดยไม่จอดรถแช่ไว้ เนื่องจากซอยแคบ ดังนั้นการมาจอด (arrive) และการรับรถ (depart)จะเป็นลักษณะของ stack เงื่อนไขคือ ในการรับรถ x ใดๆอยากให้ลำดับรถเป็นเหมือนเดิม ดังรูป simulate การจอดรถในที่จอดรถของนาย ก โดยใช้ operation ของ stack ข้างล่างเป็นตัวอย่าง output

การรับ input : รับ input 4 ค่าใน 1 บรรทัดโดยให้แยกโดย " " (space bar) โดยตำแหน่งแรกคือ จำนวนสูงสุดที่รถสามารถจอดได้ในซอยของ นาย ก ตำแหน่งที่สองคือ รถที่จอดอยู่ในซอยของ นาย ก ตำแหน่งที่สามคือ การกระทำเช่น ถ้าเป็น arrive จะทำการเพิ่มรถในซอย ส่วน depart จะทำการเอารถออกจากซอย โดยรถที่จะทำการเพิ่มหรือนำออกนั้นจะเป็น เลขในตำแหน่งที่ 4

***หมายเหตุ ถ้าในซอยไม่มีรถอยู่เลยให้ input = 0 ในตำแหน่งที่ 2***

*** สามารถสร้างได้มากกว่า 1 stack ***'''

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

a = Stack()
b = Stack()

print("******** Parking Lot ********")
m,s,o,n = input("Enter max of car,car in soi,operation : ").split()
m,n = int(m),int(n)

if s == '0':
  pass
else:
  cars = s.split(',')
  for data in cars:
    a.push(int(data))
if o == 'arrive':
  if a.size() < m:
    if str(n) not in s.split(','):
      a.push(n)
      print('car',n,'arrive! : Add Car',n)
    else:
      print('car', n ,'already in soi')
  else:   
    print('car',n,'cannot arrive : Soi Full')
elif o == 'depart':
  if a.size() == 0:
    print('car',n, 'cannot depart : Soi Empty')
  else:
    found = False
    while not a.isEmpty():
      if a.peek() == n:
        found = True
        break
      else:
        b.push(a.pop())
    if found:
      print('car', n ,'depart ! : Car' , n ,'was remove')
      a.pop()
      while not b.isEmpty():
        a.push(b.pop())
    else:
      print('car', n ,'cannot depart : Dont Have Car',n)
      while not b.isEmpty():
        a.push(b.pop())
print(a)
