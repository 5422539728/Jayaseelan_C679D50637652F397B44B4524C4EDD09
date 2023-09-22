class student():
  def __init__(self,name,roll,cgpa):
       self.name=name
       self.roll=roll
       self.cgpa=cgpa

def sortcgpa(sortlist):
  sortedstu=sorted(sortlist, key=lambda x: x.cgpa, reverse=True)
  return sortedstu

stuobj=[student("Harishkumar","22CS2110",8.9),student("Inbarajan","22CS2111",8.5),student("Jayaseelan","22CS2112",6.3),student("kalaiselvan","22CS2114",9.8)]
sortedstu=sortcgpa(stuobj)

for stu in sortedstu:
  print(f"Name: {stu.name}   Roll.no: {stu.roll}    CGPA: {stu.cgpa}")