'''รับ string มาเข้าคิวหา secret code โดยรับ input คือ

code เป็น string ยาว

hint คือตัวแรกของรหัสที่ถูกต้อง



**คำใบ้**

ascii ของ "f" มีค่า = 102

ascii ของ "g" มีค่า = 103

ascii ของ "h" มีค่า = 104

ascii ของ "i" มีค่า = 105

ascii ของ "j" มีค่า = 106'''
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

s  = input('Enter code,hint : ').split(',')
code = []
code.extend(s[0])
hint = s[1]
decode =ord(hint) - ord(code[0]) 
q = Queue()
for i in range(len(code)):
  q.enQueue(chr(ord(code[i]) + decode))
  print(q)
