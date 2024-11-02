Week 4: Object oriented programming, Linear data structures
_____________________________________________________________________________

__Class definition__
Class RobotTurtle:
    def __init__(self, name, speed = 1):
        self._name = name
        self._speed = speed
        self._pos = (0,0) 

    def move(self, direction): # update property in the function
        update = {
                'up': (self._pos[0], self._pos[1]+ self._speed),
                'left': (self._pos[0] -1, self._pos[1] ),
                'right': (self._pos[0] +1, self._pos[1]),
                'down': (self._pos[0], self_pos[1]-1)
            }
        self._pos = update[direction]

    def tell_name(self): #defining a return function
        return f"my name is {self._name}"

    @property
    def name (self): # property getter
        return self._name

    @name.setter 
    def name(self, value): # property setter
        if isinstance(value, str) and value != "":
            self._name = value


__creating an object__
my_robot = RobotTurtle("T1")  #this is instantiating an object, arguement is then passed onto the init function to formally initiate the object

__calling methods in objects__
object.method_name(arguement)
e.g. my_robot.tell_name()


__Encapsulation of properties__
# purpose is to make sure that no one fucks with the properties of the object, breaking the code
# "would be a shame if someone tried to divide by 0"
____________________________________________________________________________

__Special Methods__
# Some methods in python can be overwritten through overloading.
# E.g. __init__ function is an example of overloading


#another one is 

__str__(self):
    return f"{self.x}, {self.y}"
#this string returns back properties x and y when object is called

______________________________________________________________________________

__Linear data structures__

1. Stack (LIFO)
Functions: Push, Pop, Peek

Class Stack:
    def __init__(self):
        self.__item: list[Any] =[]

    def push(self, item) -> None:
        self.stack1.append(item)

    def.pop(self) -> Any:
        if self.__item != 0:
            val = self.__item[-1]
            del self.__item[-1]
            return val
        else:
            return None

    def peek(self)-> Any:
        return self.__item[-1]
    
    @property
    def isempty(self):
        if len(self.__item) == 0:
            return True
        else: 
            return False
    
    @property
    def size(self):
        return len(self.__item)

2. Queue (FIFO)
Functions: Enqueue, Dequeue, Peek

Class Queue:
    def __init__(self):
        self.left_stack: Stack = Stack()
        self.right_stack: Stack = Stack()
        self.is_empty = self.left_stack.is_empty
        self.size = self.left_stack.size

    def enqueue(self, item):
        self.left_stack.push(item)
        self.update()
