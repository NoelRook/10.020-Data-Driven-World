Week 5: Inheritance and introduction to graph
_____________________________________________________________________________
__Inheriting a class__
class NameSubClass(NameBaseClass):
    # child class inherits all the methods and attributes from the parent class
    def__init(self):

__Example: Mixed Fraction Class__
[Fraction_Parent]
Attributes:
    Numerator
    Denominator
Functions:
    __init(self, top, bot, whole=0)__
    __str__(self)
    __add__(self,other)
    __sub__(self, other)
            |
            |
            |
[MixedFraction_Child]
Attributes:
    (inherited from parents)
    Numerator = whole * bottom + top
Functions:
    __init(self, top, bot, whole=0)__
    __str(self)__

# mixed fraction inherits its attributes from its parent, Fraction (Useful for methods like addition and subtraction)

# __str()__ method is overriden for the mixedFraction_child so that its represented differently

__Queue & Deque__

# Deque(pronounced deck) is the opposite of queue
# Deque's items are inserted from the front/rear, and can be poped from the front/rear

[Class_Queue]
Attributes: 
    left_stack
    right_stack
    /is_empty
    /size
Functions:
    __init__()
    enqueue(item)
    dequeue():item
    peek():item
            |
            |
            |
            |
[Class_Deque]
Attribute:
    (inherits all from parent)
Functions:
    add_front(item)
    add_rear(item)
    remove_front():item
    remove_rear():item
    peek_front():item
    peek_rear():item



__Basics of a Graph__
# Use a dictionary & OOP to represent a graph
# define grpah, vertices, edges and weights
# define directed and undirected graphs
# define paths
# Adjacency-lists, Adjacency-Matrix


Definitions:
[Vertex]: Node that is connected by edges on a graph 
[Edge]: Represented by line connecting two vertices. Can be uni-directional/ bi-directional. 

__Adjacency List__
[example]
graph1 = {'V1': ['V2', 'V5'],
          'V2': ['V1', 'V3', 'V4'],
          'V3': ['V2'],
          'V4': ['V1', 'V3'],
          'V5': ['V4']}


__Putting it all together: Racing car__

Class RacingCar:
    def __init__(self, name:str, max_speed:int)-> None:
        self.racer:str = name
        self.max_speed:int =max_speed
        self.finish:int = -1
        self.pos = 0

    @property
    def racer(self) -> str: # Getter function for racer 
        return self._racer
    
    @racer.setter
    def racer(self, name:str) -> None: @ setter function for racer
        if isinstance(name,str) and name!="":
            self._racer = name

    @property
    def speed(self)-> int: # getter function for speed
        return self._max_speed
    
    @speed.setter
    def speed(self, val:int) -> None: # setter function for racer
        if val>0 and val <= self.max_speed:
            self._max_speed = val

    @property
    def pos(self) -> int:
        return self._pos
    
    @pos.setter
    def pos(self, val:int) -> None:
        if val>=0:
            self._pos = val

    @property
    def is_finished(self) -> bool:
        if self.pos >= self.finish >0:
            return True
        else:
            return False

    def start(self, init_speed:int, finish_dist:int) ->None:
        if self.speed <=self.max_speed:
            self.speed = init_speed
        if finish >=0:
            self._pos = 0
            self.finish = finish_dist
    
    def race(self, acc:int)-> None:
        new_speed = self.speed+ acc
        self.speed = new_speed
        self.pos = self._pos + new_speed
    
    def __str__(self) -> str:
        return f"Racing Car {self.racer} at position: {self.pos}, with speed {self.speed}."


__Racing Game__

Class RacingGame:
    def __init__(self, seed:number)->None:
        self.car_list = dict[str,  RacingCar] = {}
        self._winners:list[str] = []
        random.seed(seed)

    @property
    def winner(self) -> Optional[list[str]]:
        if len(self._winners) != 0:
            return self._winners
        else:
            return None
    
    def add_car(self, name:str, speed:int) -> None:
        for i,v in enumerate(self.car_list.keys)
            self.car_list[keys].speed = random.randint(0,50)
            self.car_list[keys].finish = finish

    def play(self, finish:int) -> None:
        self.start(finish)
        finished_car:int = 0
        while True: 
            for racer, car in self.car_list.items():
                if not car.is_finished:
                    acc: int = random.randint(-10,20)
                    car.race(acc)
                    if car.is_finished:
                        self._winners.append(racer)
                        finished_car+=1
            if finished_car == len(self.car_list):
                break


__Evaluate Post fix__
Class EvaluatePostfix:
    operands: str = "0123456789"
    operators: str = "+-*/"

    def __init__self -> None:
        self.expression: list[str] = [] # list containing the operators
        self.stack: Stack = Stack() # list containing the operators

    def input(self,item:str)-> None:
        if item in self.operands or item in self.operators:
            self.expression.append(item)

    def evaluate(self) -> Number:
        for i in range(len(self.expression)):
            if self.expression[i] in self.operands:
                self.stack.push(self.expression[i])
            else:
                rightly = self.stack.pop()
                statement = str(self.stack.pop()) + self.expression[i] + str(rightly)
                self.stack.push(eval(statement))
        return self.stack.peek()



    