# data
# You can fill whatever data u whant
from tabulate import tabulate

elevatorCapacity = 3
lPeople = [
    [],
    [   4,	4,	3,	2, 2   ],
    [   3,	1,		    ],
    [   4,	4,	2,	1   ],
    [   3,	2,	1,	1   ],
]

# Reversing a list
for row in lPeople:
    row.sort(reverse=True)


# Cheking if lPeople is empty
def check():
    for i in lPeople:
        if i:
            return True
    return False

# main Elevator class
class Elevator:

    direction = 1 # direction can be 1 - up   or -1 down
    toFloor = 1
    places = []
    atFloor = 1
    def __init__(self, capacity, maxFloor):
        self.capacity = capacity
        self.available = capacity
        self.maxFloor = maxFloor
        self.arrivedFloor = [0] * (maxFloor+1)

    def unloadPeople(self):
        while self.atFloor in self.places:
            self.places.pop(self.places.index(self.atFloor))
            self.arrivedFloor[self.atFloor]+=1
        self.available = self.capacity - len(self.places)

    # diraction controll
    def dir(self):
        if self.atFloor == self.maxFloor:
            self.direction = -1
        elif self.atFloor == 1:
            self.direction = 1

    # loading people form new floor
    def newFloor(self):
        res = 0
        for val in lPeople[self.atFloor]:
            if val < self.atFloor:
                res = lPeople[self.atFloor].index(val)
                break

        self.dir()
        self.unloadPeople()

        back = res+self.available
        if back > len(lPeople[self.atFloor]):
            back = res+self.capacity
       
        front = res-self.available
        if front < 0:
            front = 0

        up = lPeople[self.atFloor][res:back]
        down = lPeople[self.atFloor][front:res]

        l = len(lPeople[self.atFloor])

        # if lisft is empty
        if not self.places:
            if l-res > res:
                del lPeople[self.atFloor][res:back]
                for i in up:
                    self.places.append(i)
                self.available = self.capacity - len(self.places)
                self.direction = -1
                if self.places: 
                    self.toFloor = min(self.places)
                if(self.atFloor+self.direction!=0):
                    self.atFloor = self.atFloor+self.direction
            else:
                del lPeople[self.atFloor][front:res]
                for i in down:
                    self.places.append(i)
                self.available = self.capacity - len(self.places)
                self.direction = 1
                if self.places: 
                    self.toFloor = max(self.places)
                if(self.atFloor+self.direction!=0):
                    self.atFloor = self.atFloor+self.direction
        else:
            del lPeople[self.atFloor][front:res]
            if self.direction ==1:
                for i in down:
                    self.places.append(i)
                self.available = self.capacity - len(self.places)
                if self.places: 
                    self.toFloor = max(self.places)
                self.atFloor = self.atFloor+self.direction
            else:
                del lPeople[self.atFloor][res:back]
                for i in up:
                    self.places.append(i)
                self.available = self.capacity - len(self.places)
                if self.places:
                    self.toFloor = min(self.places)
                self.atFloor = self.atFloor+self.direction
        

e = Elevator(elevatorCapacity,len(lPeople)-1)

while check() or e.places:
    print('______________________________________________________')
    e.newFloor()
    for x in range(1,len(lPeople)): 
        if e.atFloor==x:
            print (e.arrivedFloor[x],"  |  ", e.places, ((e.capacity-len(e.places)+1)*4-1)*".",  " | " , lPeople[x])
        else:
            print (e.arrivedFloor[x],"  |  ", e.capacity*4*".", " | ", lPeople[x])
            Ё