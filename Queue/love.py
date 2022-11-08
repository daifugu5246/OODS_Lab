'''สมมติว่านักศึกษาแอบชอบคนๆหนึ่งอยู่ โดยที่นักศึกษาและคนๆนั้นจะมีกิจกรรมและสถานที่ที่ไปแตกต่างกันในแต่ละวัน
ให้นักศึกษาเขียนโปรแกรมที่จะหาว่าสิ่งที่นักศึกษาและคนๆนั้นทำในแต่ละวันจะทำให้ได้คบกันหรือไม่ โดยใช้ Queue

กิจกรรม                                       สถานที่
0 = กินข้าว(Eat)                           0 = ร้านอาหาร(Res.)
1 = เล่นเกม(Game)                      1 = ห้องเรียน(ClassR.)
2 = ทำโจทย์ datastruc(Learn)      2 = ห้างสรรพสินค้า(SuperM.)
3 = ดูหนัง(Movie)                        3 = บ้าน(Home)

โดยการรับ Input จะประกอบด้วย

กิจกรรม:สถานที่(ของนักศึกษาและของคนๆนั้น) โดยในแต่ละวันจะคั่นด้วยเครื่องหมาย ,

เช่น วันที่ 1 นักศึกษาไปกินข้าวที่ร้านอาหาร และ คนๆนั้นไปนั่งทำโจทย์ datastruc ที่ร้านอาหาร 
       วันที่ 2 นักศึกษาไปเล่นเกมที่บ้าน และ คนๆนั้นไปดูหนังที่ห้างสรรพสินค้า
จะได้ว่า 0:0 2:0,1:3 3:2

***มีการคิดคะแนนดังนี้***

·       กิจกรรมเดียวกันแต่คนละสถานที่         +1

·       สถานที่เดียวกันแต่ทำกิจกรรมต่างกัน    +2

·       กิจกรรมเดียวกันและสถานที่เดียวกัน    +4

·       ไม่เหมือนกันเลย                                   - 5

หากมีคะแนนมากกว่าหรือเท่ากับ 7 จะถือว่าได้คบกัน แต่ถ้าคะแนนน้อยกว่า 7 แต่มากกว่า 0 เป็นคนคุย น้อยกว่านั้นถือว่าเป็นได้แค่เพื่อน

โดยในแต่ละขั้นตอนให้แสดงผลดังตัวอย่าง'''
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


def changeToString(q = Queue()):
  actdict = {
  '0' : 'Eat',
  '1' : 'Game',
  '2' : 'Learn', 
  '3' : 'Movie'
  }

  placedict = {
    '0' : 'Res.',
    '1' : 'ClassR.',
    '2' : 'SuperM.', 
    '3' : 'Home'
  }
  for data in q.list[:]:
    temp = q.deQueue().split(':')
    temp[0] = actdict[temp[0]]
    temp[1] = placedict[temp[1]]
    s = temp[0] + ':' + temp[1]
    q.enQueue(s)
  return q.list


def scoreCal(me = Queue(),her = Queue()):
  score = 0
  for i in range(me.size()):
    temp = me.list[i].split(':')
    act_me = temp[0]
    place_me = temp[1]
    temp = her.list[i].split(':')
    act_her = temp[0]
    place_her = temp[1]
    if act_me == act_her and place_me == place_her:
      score += 4
    elif act_me == act_her and place_me != place_her:
      score += 1
    elif act_me != act_her and place_me == place_her:
      score += 2
    else:
      score -= 5
  else:
    if score >= 7:
      status = "Yes! You're my love! : Score is {s}.".format(s = score)
    elif score < 7 and score > 0:
      status = "Umm.. It's complicated relationship! : Score is {s}.".format(s = score)
    else:
      status = "No! We're just friends. : Score is {s}.".format(s = score)
      
  return status

inp = input('Enter Input : ').split(',')
me = Queue()
her = Queue()
for data in inp:
  tmp_1 = data.split()
  me.enQueue(tmp_1[0])
  her.enQueue(tmp_1[1])
print('My   Queue = ',end = '') 
print(*me.list,sep = ', ')
print('Your Queue = ',end = '') 
print(*her.list,sep = ', ')
print('My   Activity:Location = ' ,end='')
print(*changeToString(me), sep = ', ')
print('Your Activity:Location = ', end = '') 
print(*changeToString(her), sep = ', ')
print(scoreCal(me,her))
  
