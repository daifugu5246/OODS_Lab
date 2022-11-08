'''เกม Color Crush คืออะไร : Color Crush จะเป็นเกมที่นำสีมาเรียงต่อกัน โดยสีจะหายไปก็ต่อเมื่อมีการเรียงสีเหมือนกันครบ 3 อัน เช่น  ABBBA  -> AA  เนื่องจาก B เรียงติดกัน 3 ตัวทำให้ระเบิดหายไปโดยที่สีจะมีทั้งหมด 26 สี และจะถูกแทนด้วย A - Z  ถ้าหากมีการเรียงกันแบบ  ABBBAA -> Empty  เนื่องจาก  ถ้าหาก B ระเบิด  A(BBB)AA -> AAA จะเห็นว่า A ก็เรียงกันอีก 3 ตัวทำให้เกิดการระเบิดขึ้นอีกครั้งหนึ่ง  และถ้าหากมีการเรียงกันแบบ AAAA -> A เนื่องจากมีการเรียงกัน 3 ตัว  (AAA)A ทำให้เหลือ A 1 ตัว



เนื้อเรื่อง :  หลังจากที่กฤษฎาได้เล่นเกม Color Crush ก็ได้ไปเห็นโฆษณาว่า บริษัทที่ได้สร้าง Color Crush มีแผนการที่จะสร้างเกม Color Crush 2 ขึ้นมา กฤษฎาจึงได้สมัครเข้าไปร่วมทีมในการสร้างเกม Color Crush 2 ซึ่งเกมนี้จะมีกิมมิคที่แตกต่างออกไป คือการที่จะมี 2 ฝั่ง คือ ฝั่งปกติกับฝั่งโลกกระจก โดยฝั่งโลกกระจกจะเกิดการระเบิดก่อน ซึ่งการระเบิดของฝั่งโลกกระจกจะไม่ใช่ระเบิดแล้วหายไปเลย แต่จะเป็นระเบิดแล้วกลายเป็น ITEM ไว้สำหรับขัดขวางการระเบิดของฝั่งปกติ  หลังจากที่ฝั่งโลกกระจกเกิดการระเบิดครบแล้ว ก็จะเป็นคิวของฝั่งปกติ  ซึ่งถ้าหากฝั่งปกติมีการเรียงกันของสีที่จะทำให้เกิดการระเบิด ในเสี้ยววินาทีนั้นก่อนที่จะเกิดการระเบิดของฝั่งปกติ  ITEM สำหรับขัดขวางการระเบิดของฝั่งโลกกระจก จะมาคั่นระหว่างระเบิดลูกที่ 2 กับ ลูกที่ 3 (อาจจะทำให้เกิดการระเบิดเหมือนเดิมได้ถ้าหาก ระเบิดนั้นเป็นสีเดียวกัน  แต่ถ้าเป็นคนละสีก็จะทำให้ไม่เกิดการระเบิดขึ้น)  โดยระเบิดอาจจะเกิดการระเบิดซ้อนๆกันเรื่อยๆได้จะเป็น Empty  เช่น ถ้าหากฝั่งปกติมีระเบิดเรียงแบบนี้ AAAAA และฝั่งโลกกระจกมีระเบิดแบบนี้ AAA ถ้าหากฝั่งปกติระเบิดธรรมดา 1 ทีจะเหลือแค่ AA แต่ถ้าหากฝั่งโลกกระจกมาขัดขวาง จะกลายเป็น AA(A)AAAA ก็จะเกิดระเบิด 2 ทีทำให้ระเบิดฝั่งปกติเป็น Empty



อธิบายรูปแบบ Input ของ Test_Case_1 : ฝั่งปกติจะมีระเบิดเรียงดังนี้ -> AAABBBCDEE  ฝั่งโลกกระจกจะมีระเบิดเรียงดังนี้ -> HHH โดยฝั่งโลกกระจกจะมีระเบิด H ที่เป็น ITEM สำหรับขัดขวาง 1 ลูกไว้สำหรับขัดขวางการระเบิดที่จะเกิดขึ้นกับฝั่งปกติได้  ต่อมาฝั่งปกติจะเกิดการระเบิดของ A และ B ตามลำดับ  โดยฝั่งโลกกระจกจะนำระเบิด H ไปขัดขวางการระเบิดของระเบิด A เพราะระเบิด A เกิดการระเบิดก่อนระเบิด B  โดยการขัดระเบิดนั้นจะเป็นการขัดระหว่างลูกที่ 2 กับลูกที่ 3 เพื่อให้เห็นภาพ -> AAABBBCDEE -> AA(H)ABBBCDEE  -> AA(H)ACDEE ลำดับจะเป็นดังนี้  และฝั่งปกติเกิดการระเบิด 1 ครั้ง ส่วนฝั่งโลกกระจกก็เกิดการระเบิดอีก 1 ครั้ง



อธิบายรูปแบบ Input ของ Test_Case_3 : ฝั่งปกติจะมีระเบิดเรียงดังนี้ -> AAABBBCDDDEE  ฝั่งโลกกระจกจะมีระเบิดเรียงดังนี้ -> BBBTENETAAA โดยฝั่งโลกกระจกจะมีระเบิด A และ B ที่เป็น ITEM สำหรับขัดขวาง 2 ลูกตามลำดับไว้สำหรับป้องกันการระเบิดที่จะเกิดขึ้นกับฝั่งปกติได้  ต่อมาฝั่งปกติจะเกิดการระเบิดของ A B และ D ตามลำดับ  โดยฝั่งโลกกระจกจะนำระเบิด A  ไปขัดขวางการระเบิดของระเบิด A เพราะระเบิด A เกิดการระเบิดก่อนระเบิด B  โดยการขัดระเบิดนั้นจะเป็นการขัดระหว่างลูกที่ 2 กับลูกที่ 3  เพื่อให้เห็นภาพ -> AAABBBCDDDEE -> AA(A)ABBBCDDDEE -> ABBBCDDDEE ลำดับจะเป็นดังนี้  ต่อมาจะนำระเบิด B ไปขัดขวางการระเบิดของระเบิด B เพื่อให้เห็นภาพ  ABBBCDDDEE -> ABB(B)BCDDDEE -> ABCDDDEE  ต่อมาเกิดการระเบิดอีก 1 ครั้ง ABCDDDEE -> ABCEE ซึ่งฝั่งโลกกระจกไม่สามารถขัดขวางได้เพราะ ITEM สำหรับขัดขวางหมดแล้ว   และฝั่งปกติเกิดการระเบิดทั้งหมด 3 ครั้ง  ซึ่ง 2 ครั้งเกิดจากการที่ฝั่งโลกกระจกใส่ระเบิดสีเดียวกันมาซึ่งถือว่าเป็นการขัดขวางที่ผิดหและเกิดการระเบิดเองอีก 1 ครั้ง ส่วนฝั่งโลกกระจกก็เกิดการระเบิดอีก 2 ครั้ง



อธิบายรูปแบบ Output : แบ่งออกเป็น 2 ฝั่งคือฝั่งปกติกับฝั่งโลกกระจก  โดยบรรทัดแรกจะเป็นจำนวนระเบิดที่เหลืออยู่ บรรทัดที่สองจะเป็นระเบิดที่เหลืออยู่แต่ถ้าหากไม่มีระเบิดเหลืออยุ่เลยให้แสดง "Empty" บรรทัดที่สามจะเป็นจำนวนที่เกิดระเบิดขึ้น บรรทัดที่สี่จะมีเฉพาะฝั่งปกติถ้าหากเกิดเหตุการณ์ที่ ITEM ของฝั่งโลกกระจกมาขัดขวาง แต่ระเบิดนั้นดันเป็นลูกเดียวกับที่จะเกิดการระเบิด  ส่วนทีมสีน้ำเงินจะเหมือนกับทีมสีแดงแต่บรรทัดที่ 2 กับ 3 และชื่อทีม จะเป็นแบบ inverse



คำใบ้ - ใช้ Stack ในการหาลูกระเบิดเรียงกัน 3 ลูก   โดยให้ทำฝั่งโลกกระจกก่อนว่ามีระเบิดลูกอะไรบ้าง (ก่อนเข้า stack ให้ Reverse ก่อน)  จากนั้นเก็บลง Queue แล้วไปทำฝั่งปกติถ้าหากฝั่งปกติเกิดการระเบิดก็ DeQueue ระเบิดที่ได้รับมาจากฝั่งกระจกมาขัดระเบิดระหว่างลูกที่ 2 กับ 3

อธิบาย Case 10:

ฝั่งซ้าย = DDDFFFGGG
ฝั่งขวา = ABBBAACCC
ทำฝั่งขวาก่อนโดยการ inverse ABBBAACCC -> CCCAABBBA จะได้ระเบิดมา 3 ลูกคือ C B A ตามลำดับจากนั้นเก็บลง Queue ต่อมาดูที่ฝั่งซ้าย DDD จะเกิดการระเบิดเราจะนำ C ไปขัด | ต่อมา F จะระเบิดเราจะนำ B มาขัด | ต่อมา G จะระเบิดเราจะนำ A มาขัด   สุดท้ายจะกลายเป็น DDCDFFBFGGAG'''
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

  def insert(self,item):
    return self.list.insert(2,item)
    
  def front(self):
    return self.list[0]

  def rear(self):
    return self.list[-1]
  
  def isEmpty(self):
    return self.list == []

  def size(self):
    return len(self.list)

  def reverse(self):
    self.list = self.list[::-1]
    
  def __str__(self):
    return str(self.list)

class Stack:
  def __init__(self,L=None):
    if L == None:
      self.list = []
    else:
      self.list = L

  def push(self,data):
    self.list.append(data)

  def pop(self):
    return self.list.pop()

  def peek(self):
    return self.list[-1] 

  def isEmpty(self):
    return self.list == []

  def size(self):
    return len(self.list)

  def reverse(self):
    self.list = self.list[::-1]
    
  def __str__(self):
    return str(self.list)

def reverseString(s = ''):
  return s[::-1]


inp = input('Enter Input (Normal, Mirror) : ').split()
norm = []
norm.extend(inp[0])
mirr = []
mirr.extend(inp[1])

mirr.reverse()
mirr = Queue(mirr)
norm = Queue(norm)

#mirr_explosive
item  = Queue()
left_color1 = Stack()
temp = mirr.deQueue()
count1 = 1
mirr_explo = 0
while not mirr.isEmpty():
  if mirr.front() == temp:
    count1 += 1
    mirr.deQueue()
    #debug when deQ make mirr empty and do not push left color.
    if norm.isEmpty():
      for i in range(count1):
        left_color1.push(temp)
  else:
    for i in range(count1):
      left_color1.push(temp)
    temp = mirr.deQueue()
    count1 = 1
    #debug last element
    if mirr.isEmpty():
      left_color1.push(temp)

  if count1 == 3:
    mirr_explo += 1
    item.enQueue(temp)
    '''when push item push color in left_color back to mirr for check explosive case again'''
    mirr.reverse()
    while not left_color1.isEmpty():
      #debug when perfect explosive
      mirr.enQueue(left_color1.pop())
    else:
      mirr.reverse()
    if not mirr.isEmpty():
      temp = mirr.deQueue()
      count1 = 1
      if mirr.isEmpty():
        left_color1.push(temp)
  
#normal_explosive
left_color2 = Stack()
temp = norm.deQueue()
count2 = 1
norm_explo = 0
count_fail = 0
while not norm.isEmpty():
  if norm.front() == temp:
    count2 += 1
    norm.deQueue()
    #debug when deQ make norm empty and do not push left color.
    if norm.isEmpty() and count2 != 3:
      for i in range(count2):
        left_color2.push(temp)
  else:
    for i in range(count2):
      left_color2.push(temp)
    temp = norm.deQueue()
    count2 = 1
    #debug last element
    if norm.isEmpty():
      left_color2.push(temp)
      
  if count2 == 3 :
    if item.isEmpty():
      norm_explo += 1
      norm.reverse()
      '''when push item push color in left_color back to mirr for check explosive case again'''
      while not left_color2.isEmpty():
        #debug when perfect explosive
        if norm.isEmpty(): 
          left_color2.pop()
        else:
          norm.enQueue(left_color2.pop())
      else:
        norm.reverse()
      if not norm.isEmpty():
        temp = norm.deQueue()
        count2 = 1
        if norm.isEmpty():
          left_color2.push(temp)
    else:
      norm.reverse()
      for i in range(count2):
        norm.enQueue(temp)
      norm.reverse()
      norm.insert(item.deQueue())
      #check success of item
      temp = norm.deQueue()
      tmp = Stack()
      tmp.push(temp)
      itr_fail = False
      for i in range(2):
        if norm.front() == temp:
          itr_fail = True
          tmp.push(norm.deQueue())
        else:
          tmp.push(norm.deQueue())
          itr_fail = False
          break
      if itr_fail:
        count_fail += 1
        while not tmp.isEmpty():
          tmp.pop()
      else:
        norm.reverse()
        while not tmp.isEmpty():
          norm.enQueue(tmp.pop())
        norm.reverse()
      temp = norm.deQueue()
      count2 = 1

left_color2.reverse()
mirr_left = ''.join(left_color1.list)
norm_left = ''.join(left_color2.list)
if mirr_left == '':
  mirr_left = 'Empty'
  
if norm_left == '':
  norm_left = 'Empty'

print('NORMAL :')
print(left_color2.size())
print(norm_left)
print(f'{norm_explo} Explosive(s) ! ! ! (NORMAL)')
if count_fail > 0:
  print(f'Failed Interrupted {count_fail} Bomb(s)')
else:
  pass
print('------------MIRROR------------')
print(': RORRIM')
print(reverseString(str(left_color1.size())))
print(reverseString(mirr_left))
print(f'(RORRIM) ! ! ! (s)evisolpxE {mirr_explo}')
