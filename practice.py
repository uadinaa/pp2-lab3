class Person:
  def __init__(self, nam, ag):
    self.nam = nam
    self.ag = ag

p1 = Person("John", 36)
print(p1.nam)
print(p1.ag)


class classm:
  def __init__(d, student, mark):
    d.student = student
    d.mark = mark

  def __str__(d):
    return f"{d.student} {d.mark}"

student = input()
mark = int(input())

p2 = classm(student, mark)

#print(p2.student)
#print(p2.mark)

print(p2)
print(type(p2))



class MyClass:
  x = 5
class cla:
  y = 3904
p1 = MyClass()
p2 = cla()

print((p1.x )+(p2.y))
