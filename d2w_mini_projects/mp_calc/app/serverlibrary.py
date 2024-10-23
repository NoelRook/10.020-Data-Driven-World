





def get_smallest_three(challenge):
  records = challenge.records
  times = [r for r in records]
  mergesort(times, lambda x: x.elapsed_time)
  return times[:3]


def merge(array: list, p: int, q: int, r: int, byfunc =None) -> None: #modified mergsort
    left_array = array[p:q+1]
    right_array = array[q+1:r+1]
    left =right = 0
    dest = p
    while left<len(left_array) and right<len(right_array):
        if byfunc != None: 
            curTupleLeft = byfunc(left_array[left])
            curTupleRight = byfunc(right_array[right])
        else:
            curTupleLeft = left_array[left]
            curTupleRight = right_array[right]
        if curTupleLeft<= curTupleRight: # add change here
            array[dest]= left_array[left]
            left = left +1
        else:
            array[dest]= right_array[right]
            right=right+1
        dest = dest+1
    while left<len(left_array):
        array[dest] = left_array[left]
        left=left+1
        dest=dest+1
    while right <len(right_array):
        array[dest]= right_array[right]
        right = right +1
        dest=dest+1
                    
            
def mergesort_recursive(array: list, p: int, r: int, byfunc =None) -> None:
     if r-p>0:
        q = (p+r)//2
        mergesort_recursive(array, p, q,byfunc)
        mergesort_recursive(array, q+1, r,byfunc)
        merge(array,p,q,r, byfunc)

def mergesort(array, byfunc=None):
    mergesort_recursive(array, 0, len(array), byfunc)
    pass


class Stack: # implement stack
  def __init__(self, first=None):
      self.stackls = list()
      if first != None:
          self.push(first)
  def push(self, thingy):
      self.stackls.append(thingy)
  def pop(self):
      if not self.is_empty:
          return self.stackls.pop()
      return None
  def peek(self):
      if not self.is_empty:
          return self.stackls[-1]
      return None
  @property
  def is_empty(self):
      return len(self.stackls)==0
  @property
  def size(self):
    return len(self.stackls)

class EvaluateExpression: #eval expression
  valid_char = '0123456789+-*/() '
  operators = '+-*/()'
  def __init__(self, string=""):
    self.strings = string

  @property
  def expression(self):
    return self.strings

  @expression.setter
  def expression(self, new_expr):
    if all(char in self.valid_char for char in new_expr):
      self.strings = new_expr
    else:
      self.strings = ""

  def insert_space(self) ->str:
    spacedString = ""
    for i in range(len(self.strings)):
      if self.strings[i] in self.operators:
        spacedString += " " + self.strings[i] + " "
      else:
        spacedString += self.strings[i]
    return spacedString

  def process_operator(self, operand_stack, operator_stack):
    righty ,ops = operand_stack.pop(), operator_stack.pop()
    if ops == "/":
      statement = str(operand_stack.pop()) + "//" + str(righty)
    else:
      statement = str(operand_stack.pop()) + ops +  str(righty)
    operand_stack.push(eval(statement))

  def evaluate(self):
    operand_stack = Stack()
    operator_stack = Stack()
    expression = self.insert_space()
    tokens = expression.split()
    for i in range(len(tokens)):
      if tokens[i] not in self.operators: # if extracted character is operand, push to operand stack
        operand_stack.push(tokens[i])
      
      # if extracted operator is + or , process all at operator_stack as long as operator stack is not empty and top of stack is not ()
      if tokens[i] == "+" or tokens[i] == "-": 
        if not operator_stack.is_empty and operator_stack.peek() != "(" and  operator_stack.peek() != ")":
          self.process_operator(operand_stack, operator_stack)
        operator_stack.push(tokens[i])
      
      # if extracted operator is * or /, process all operators at the top of the operator stack and push extracted oprator to operator stack
      if tokens[i] == "*" or tokens[i] == "/":
        if operator_stack.peek() == "*" or operator_stack.peek() == "/":
            self.process_operator(operand_stack, operator_stack)
        operator_stack.push(tokens[i])
      
      #push extracted character ( to operator_stack
      if tokens[i] == "(":
        operator_stack.push(tokens[i])
      
      if tokens[i] == ")":
        while operator_stack.peek() != "(":
          self.process_operator(operand_stack, operator_stack)
    
    while not operator_stack.is_empty:
      if operator_stack.peek() == "(":
        operator_stack.pop()
      else:
        self.process_operator(operand_stack, operator_stack)
        

    return operand_stack.peek()