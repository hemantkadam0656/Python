import queue

class superCar:
    def __init__(self, Name, top_speed):
        self.Name = Name
        self.top_speed = top_speed

    def showTopSpeed(self):
        print(self.top_speed)
    

q = queue.LifoQueue()

obj1 = superCar('Tata',155) 
obj2 = superCar('Hyundai',200) 
obj3 = superCar('maruti',120) 

q.put(obj1)
q.put(obj2)
q.put(obj3)

while not q.empty():
    obj = q.get()
    # print(q.get())
    obj.showTopSpeed()


 
 