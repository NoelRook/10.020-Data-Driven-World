Revision Session
___________________________________________________
1. Time complexity

for i in range(N): [O(n)]
    print(i)

Time complexity: O(n)
# take # of times the thing loops over

for i in range(n): [O(n)]
    for j in range(i): [O(n)]
        print(j)

Time complexity: O(n^2)
# this loops 2 times, making it n^2 number of instructions

for i in range(n//2, n): [O(n)]
    for j in range(2,n, 2^i): [O(logn)]
        print(j)
Time complexity: [O(nlogn)]

Overview: take the repeating variable and * them together

2. Recursion

def cat(a,b):
    j=[]
    if a == b :            -->  [Base_Case]
        return [a]
    else:
        return [a] + cat(a+1,b) --> [recursive_rule]



3. Object oriented programming

    a. Class definition --> blueprint to reference to create a class
    b. Class instance --> an instance of a class, containing its attributes but independant from the rest of objects

    UML Diagram --> Name, attributes, mathings

Class structure:

Class Person:
    def __init__(self, attribute_1, attribute_2 = 0.01) --> None:
        self.attribute_1:str = attribute_1
        self.attribute_2:float = attribute_2 

    @property
    def attribute_1(self)-> string:
        return self._attribute_1
        #returns the attribute on call

    @setter
    def attribute_1(self, new_attribute)-> None:
        self.attribute_1 = new_attribute
        #this sets a new attribute